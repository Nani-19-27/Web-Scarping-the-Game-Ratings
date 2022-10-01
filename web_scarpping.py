#!/usr/bin/env python
# coding: utf-8

# # Top Games Rating Web Scarping Project

# In[1]:


get_ipython().system('pip install BeautifulSoup4 ')

import requests
from bs4 import BeautifulSoup

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import warnings
warnings.filterwarnings('ignore')


# #### Website Page View Showcase.  Link in the below cell

# ![Screenshot%202022-09-30%20165351.png](attachment:Screenshot%202022-09-30%20165351.png)

# In[2]:


url_link = 'https://www.imdb.com/list/ls094225069/'   # Top 34 values page-1


# In[3]:


Req  = requests.get(url_link)


# In[4]:


Req.status_code #accepted 


# In[5]:


page = BeautifulSoup(Req.content,'lxml')


# In[6]:


Game_names = page.find_all('h3',class_='lister-item-header')


# In[7]:


## here i using list comprehension instead of for loop

Game_names_list = [p.text[4:-19].strip() for p in Game_names] 


# In[8]:


year = page.find_all('span',class_='lister-item-year text-muted unbold')


# In[9]:


years = [p.text[1:-12] for p in year]


# In[10]:


rating = page.find_all('div',class_='ipl-rating-star small')


# In[11]:


len(rating)


# In[12]:


rating[0]


# In[13]:


sample = [p.text for p in rating[0].find_all('span',class_='ipl-rating-star__rating')]

sample


# In[14]:


ratings = []

for i in range(len(rating)):
    a=[]
    for j in rating[i].find_all('span',class_='ipl-rating-star__rating'):
        a.append(j.text)
    ratings.append(','.join(a))    
    


# In[15]:


Voting = page.find_all('p',class_='text-muted text-small')


# In[16]:


len(Voting)


# In[17]:


Voting[2]


# In[18]:


sample2 = [p.text for p in Voting[2]][3]

sample2


# In[19]:


Votings =[]
i = 2

while i < len(Voting):
    d = [p.text for p in Voting[i]][3]
    Votings.append(d)
    i += 3
    


# In[20]:


import pandas as pd


# In[21]:


df = pd.DataFrame({'Year':years,'Names':Game_names_list,'Rating':ratings,'Votings':Votings})


# In[22]:


df['Votings'] = df['Votings'].str.replace('[\,\,]','').astype(int)


# In[23]:


df['Rating'] = df['Rating'].astype(float)


# In[24]:


df.head()

#Note   - Zeruda no densetsu: Buresu obu za wairudo ( The Legend of Zelda: Breath of the Wild in english)

#       - Zeruda no densetu Kaze no takuto HD ( The Legend of Zelda: The Wind Waker HD)


# In[25]:


df.info() #Page-1 , 34 games


# In[26]:


plt.figure(figsize=(25,5))

plt.title('Rating Figures Frequency',fontdict={'size':25})

plt.hist(x=df.Rating,histtype='bar',rwidth=0.98,hatch='||',)

plt.xticks(df.Rating,fontsize=20)
plt.yticks(fontsize=20);


# In[27]:


top_10_rated_games = df.sort_values('Rating', ascending =False).head(10)

plt.figure(figsize=(25,5))

plt.title('Top 10 Rated Games',fontdict={'size':27})

x= sns.barplot(x=top_10_rated_games.Names,y=top_10_rated_games.Rating,hatch='...')

plt.tick_params(labelrotation=90)

sns.despine()

plt.xticks(fontsize=20);


# In[28]:


rating_9_games = df[df['Rating']>9][['Rating','Names','Votings']].sort_values(['Rating','Votings'],ascending=[0,0])


plt.figure(figsize=(25,5))

plt.title('Above 9 Rated Games with Vote Volume',fontdict={'size':27})

sns.barplot(x=rating_9_games.Names,y=rating_9_games.Votings,hatch='...')

plt.tick_params(labelrotation=90)

sns.despine()

plt.yticks(fontsize=10)
plt.xticks(fontsize=20);


# ## Box Chart View 
# 
# Clean Understanding Between Ratings and respective Volume of Voting

# In[29]:


rating_9_games


# In[ ]:





# In[ ]:




