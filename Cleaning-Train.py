#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import numpy as np


# In[20]:


list_acc = []
list_gyr = []
data_gyr_all = pd.DataFrame()
data_acc_all = pd.DataFrame()


# In[21]:


for i in range(0,10):    
    data = pd.read_csv("/home/jovyan/Accl_data/data_"+"160"+str(i)+"_accel_phone.txt", header=None)
    list_acc.append(data)
    data = pd.read_csv("/home/jovyan/Gyro_data/data_"+"160"+str(i)+"_gyro_phone.txt", header=None)
    list_gyr.append(data)
for i in range(10,20):    
    data = pd.read_csv("/home/jovyan/Accl_data/data_"+"16"+str(i)+"_accel_phone.txt", header=None)
    list_acc.append(data)
    data = pd.read_csv("/home/jovyan/Gyro_data/data_"+"16"+str(i)+"_gyro_phone.txt", header=None)
    list_gyr.append(data)


# In[22]:


data_gyr_all = data_gyr_all.append(list_gyr,True)
data_acc_all = data_acc_all.append(list_acc,True)


# In[23]:


data_acc_all.columns=["id", "class", "t-stamp", "a-x", "a-y", "a-z"] 
data_gyr_all.columns=["id", "class", "t-stamp", "g-x", "g-y", "g-z"] 


# In[24]:


data_acc_all


# In[25]:


data_gyr_all


# In[26]:


new_df = pd.merge(data_acc_all,data_gyr_all)


# In[27]:


new_df


# In[28]:


Required = new_df.drop(columns=['id', 't-stamp'])
Required


# In[29]:


Required.to_csv('Cleaned_Train_data.csv',index=False)


# In[ ]:




