#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df=pd.read_excel("1_구어1.xlsx",encoding="utf-8")
df=df[["원문","번역문"]]
df2=pd.read_excel("1_구어2.xlsx",encoding="utf-8")
df2=df2[["원문","번역문"]]
df3=pd.read_excel("2_대화.xlsx",encoding="utf-8")
df3=df3[["원문","번역문"]]
df4=pd.read_excel("3_뉴스1.xlsx",encoding="utf-8")
df4=df4[["원문","번역문"]]
df5=pd.read_excel("3_뉴스2.xlsx",encoding="utf-8")
df5=df5[["원문","번역문"]]
df6=pd.read_excel("3_뉴스3.xlsx",encoding="utf-8")
df6=df6[["원문","번역문"]]
df7=pd.read_excel("3_뉴스4.xlsx",encoding="utf-8")
df7=df7[["원문","번역문"]]
df8=pd.read_excel("4_한국문화.xlsx",encoding="utf-8")
df8=df8[["원문","번역문"]]
df9=pd.read_excel("6_지자체웹사이트.xlsx",encoding="utf-8")
df9=df9[["원문","번역문"]]


# In[3]:


a=pd.concat([df,df2,df3,df4,df5,df6,df7,df8,df9])


# In[4]:


a.head()


# In[5]:


a.to_csv("sum.csv",encoding="utf-8")


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
df10=pd.read_csv("sum.csv",encoding="utf-8")
kl=[]
el=[]

for i in range(len(df10)):
    kl.append(len(df10["원문"][i]))
    el.append(len(df10["번역문"][i]))


# In[7]:


kl2=sorted(kl)
el2=sorted(el)
a1=pd.Series(kl)
a2=pd.Series(el)
print(a1.describe())
print(a2.describe())


# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.figure(dpi=300)
plt.subplot(1,2,1)
plt.scatter(range(len(kl2)),kl2)
plt.title("Korean")
plt.subplot(1,2,2)
plt.scatter(range(len(el2)),el2)
plt.title("English")
plt.show()


# In[8]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.figure(dpi=300)
plt.subplot(1,2,1)
plt.boxplot(kl2)
plt.title("Korean")
plt.subplot(1,2,2)
plt.boxplot(el2)
plt.title("English")
plt.show()


# In[10]:


Q1 = np.percentile(kl2, 25) 
Q3 = np.percentile(kl2, 75) 
print(Q1,Q3)
IQR = Q3 - Q1 
koutlier_step = 1.5 * IQR
print(koutlier_step)
print(Q3+koutlier_step)


# In[11]:


Q1 = np.percentile(el2, 25) 
Q3 = np.percentile(el2, 75) 
print(Q1,Q3)
IQR = Q3 - Q1 
eoutlier_step = 1.5 * IQR
print(eoutlier_step)
print(Q3+eoutlier_step)


# In[12]:


df10=pd.read_csv("sum.csv",encoding="utf-8")
index=[]

for i in range(len(df10)):
    if len(df10["원문"][i])<=148:
        if len(df10["번역문"][i])<=386:
            index.append(i)


# In[29]:


len(index)


# In[13]:


len(index)


# In[14]:


kr=[]
er=[]
for i in index:
    kr.append(df10["원문"][i])
    er.append(df10["번역문"][i])
    
    


# In[15]:


len(kr), len(er)


# In[16]:


tdf=pd.DataFrame(data={"Korean":kr, "English":er})
tdf.head()


# In[17]:


len(tdf)


# In[18]:


tdf.to_csv("final.csv",encoding="utf-8")

