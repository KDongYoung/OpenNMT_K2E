#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data=pd.read_csv("final.csv",encoding="utf-8",index_col=[0])
data.head()


# In[3]:


len(data)


# ## Test

# In[4]:


def sampling_func(data):
    N = len(data)
    sample_n=2000 # 2000개 뽑기
    sample = data.take(np.random.permutation(N)[:sample_n])
    return sample


# In[5]:


td=sampling_func(data)
td.head()


# In[6]:


len(td)


# In[7]:


with open("src-test.txt",'w',encoding="utf-8") as f:
    for k in td["Korean"]:
        f.write(k)   
        f.write("\n")   


# In[8]:


with open("tgt-test.txt",'w',encoding="utf-8") as f:
    for e in td["English"]:
        f.write(e)
        f.write("\n") 


# ## Validation

# In[8]:


ai=[]
for a in data.index:
    if a not in td.index:
        ai.append(a)
len(ai)


# In[9]:


data2=data.iloc[ai]
data2.head()


# In[10]:


with open("src-total.txt",'w',encoding="utf-8") as f:
    for k in data2["Korean"]:
        f.write(k)   
        f.write("\n")   


# In[11]:


with open("tgt-total.txt",'w',encoding="utf-8") as f:
    for e in data2["English"]:
        f.write(e)
        f.write("\n") 


# In[12]:


def sampling_func(data):
    N = len(data)
    sample_n=7000 # 7000개 뽑기
    sample = data.take(np.random.permutation(N)[:sample_n])
    return sample


# In[13]:


td2=sampling_func(data2)
td2.head()


# In[14]:


len(td2)


# In[16]:


with open("src-valid.txt",'w',encoding="utf-8") as f:
    for k in td2["Korean"]:
        f.write(k)   
        f.write("\n")   


# In[17]:


with open("tgt-valid.txt",'w',encoding="utf-8") as f:
    for e in td2["English"]:
        f.write(e)
        f.write("\n") 


# ## Train

# In[16]:


bi=[]
for a in data2.index:
    if a not in td2.index:
        bi.append(a)
len(bi)


# In[17]:


data3=data.iloc[bi]
data3.head()


# In[20]:


with open("src-train.txt",'w',encoding="utf-8") as f:
    for k in data3["Korean"]:
        f.write(k)
        f.write("\n") 


# In[21]:


with open("tgt-train.txt",'w',encoding="utf-8") as f:
    for e in data3["English"]:
        f.write(e)
        f.write("\n") 


# In[ ]:




