#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas


# In[2]:


df = pandas.read_csv("iris.csv")


# In[3]:


df.describe()


# In[4]:


doops = df.duplicated()


# In[5]:


doops


# In[6]:


sepalLength = list(df['sepalLength'])
sepalWidth = list(df['sepalWidth'])
petalLength = list(df['petalLength'])
petalWidth = list(df['petalWidth'])


# In[7]:


from matplotlib import pyplot as plt


# In[8]:


plt.boxplot(sepalLength, sym='+', vert=1, whis=1.5)


# In[9]:


df.boxplot(column='sepalLength')


# In[10]:


plt.scatter(sepalLength, petalLength)


# In[11]:


import numpy as np


# In[12]:


plt.hist(sepalWidth, bins=20)


# In[ ]:


s

