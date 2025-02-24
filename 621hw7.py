#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


from matplotlib import pyplot as plt


# In[3]:


df = pd.read_csv("video_rental.csv")


# In[4]:


df.describe()


# In[5]:


print(df)


# In[6]:


df['Gender'].value_counts()


# In[7]:


grouped = df['Income'].groupby(df['Gender'])


# In[8]:


grouped.mean()


# In[21]:


grouped2 = df['Age'].groupby(df['Gender'])


# In[22]:


grouped2.describe()


# In[23]:


grouped2.count()


# In[25]:


df.groupby(['Gender', 'Genre']).count()


# In[26]:


df.sort_values(by = ['Gender', 'Genre'])


# In[27]:


from pandas import Series, DataFrame


# In[28]:


t = df['Genre'].value_counts()


# In[29]:


print(list(t.index))
print(list(t.values))


# In[33]:


plt.bar(list(t.index), list(t.values))
plt.title('Genre')


# In[36]:


t.plot.pie()
plt.title('Genre')


# In[66]:


import pandas as pd


# In[67]:


vid_rent = pd.read_csv('video_rental.csv')


# In[68]:


len(vid_rent)


# In[69]:


vid_rent.head(10)


# In[83]:


group = vid_rent['Age'].groupby(df['Genre'])


# In[84]:


type(group)


# In[85]:


group.size()


# In[93]:


#Find average ages then group by movie genre
avg = group.mean()

#blue bar = male, orange bar = female


# In[98]:


vid_rent_summary = vid_rent.groupby(['Genre', 'Gender'])['Age'].mean().unstack()


# In[99]:


print(vid_rent_summary)


# In[100]:


vid_rent_summary.plot(kind='bar')


# In[ ]:


vid_rent_summary.plot(kind='bar')

