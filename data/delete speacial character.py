#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re
from tqdm import tqdm


# In[2]:


df = pd.read_csv("final.csv", encoding = 'utf-8',index_col=[0])


# In[3]:


copy = df.copy()


# In[4]:


copy


# In[6]:


#p = re.compile('[-=+#/\^$@*\"※~&%·ㆍ「』\\‘|\(\)\[\]\<\>“˝`\'\"…》]')
p1 = re.compile('[^ ㄱ-ㅣ가-힣a-zA-Z0-9.,?!:]')
p2 = re.compile('[^ a-zA-Z0-9.,?!:`’\']')


# In[7]:


for i in tqdm(range(len(df))):    
    m1 = p1.findall(df.loc[i, 'Korean'])
    m2 = p2.findall(df.loc[i, 'English'])
    
    if m1 or m2:
        copy.drop(df.index[i], inplace=True)


# In[8]:


copy


# In[10]:


copy.to_csv("revised_total_data.csv", index = False, encoding = 'utf-8-sig')


# In[9]:


len(copy)


# In[ ]:




