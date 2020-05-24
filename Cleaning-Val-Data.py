#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


list_acc = []
list_gyr = []
data_gyr_all = pd.DataFrame()
data_acc_all = pd.DataFrame()


# In[5]:


for i in range(34,51):    
    data = pd.read_csv("/home/jovyan/Accl_Test_data/data_"+"16"+str(i)+"_accel_phone.txt", header=None)
    list_acc.append(data)
    data = pd.read_csv("/home/jovyan/Gyro_Test_data/data_"+"16"+str(i)+"_gyro_phone.txt", header=None)
    list_gyr.append(data)


# In[6]:


data_gyr_all = data_gyr_all.append(list_gyr,True)
data_acc_all = data_acc_all.append(list_acc,True)


# In[7]:


data_acc_all.columns=["id", "class", "t-stamp", "a-x", "a-y", "a-z"] 
data_gyr_all.columns=["id", "class", "t-stamp", "g-x", "g-y", "g-z"] 


# In[24]:


data_acc_all


# In[25]:


data_gyr_all


# In[8]:


new_df = pd.merge(data_acc_all,data_gyr_all)


# In[9]:


new_df


# In[10]:


Required = new_df.drop(columns=['id', 't-stamp'])
Required


# In[11]:


Required.to_csv('Cleaned_val_data.csv',index=False)


# In[ ]:




