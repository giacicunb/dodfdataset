#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

PATH_TRAIN = "dodftrain.csv"

df_train = pd.read_csv(PATH_TRAIN,encoding = 'utf8',header = 0)


# In[3]:


print(df_train.head())


# In[15]:


labelsArray = pd.unique(df_train['label'].values)
labels = labelsArray.tolist()
#print(labels)

dictionary = {}
for i in range(0,len(labels)):
    dictionary[i] = labels[i]

print(dictionary)


# In[16]:





# In[ ]:




