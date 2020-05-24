#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


# ### Loadind Data

# In[4]:


df_train = pd.read_csv('Cleaned_Train_data.csv')
df_test = pd.read_csv('Cleaned_Test_data.csv')


# ### pre-processing

# In[5]:


X_train = df_train.iloc[:,1:]
Y_train = df_train.iloc[:,0]
X_test = df_test.iloc[:,1:]
Y_test = df_test.iloc[:,0]


# In[6]:


X_test


# In[7]:


X_test.dtypes


# #### Further Cleaning

# In[8]:


X_train = X_train.replace('\;','',regex=True).astype(float)
X_test = X_test.replace('\;','',regex=True).astype(float)


# In[9]:


X_test.dtypes


# #### Scaling

# In[10]:


sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)


# #### Reducing size of dataset to 30%

# In[11]:


from sklearn.model_selection import train_test_split


# In[12]:


X_red_train, X_extra, Y_red_train, y_extra=train_test_split(X_train,Y_train,test_size=0.7,random_state=1)


# In[13]:


Y_red_train.value_counts()


# #### Model

# In[23]:


from sklearn.ensemble import GradientBoostingClassifier as GBClassifier


# In[24]:


classifier = GBClassifier()
classifier.fit(X_red_train, Y_red_train)


#    #### Predictions

# In[34]:


y_pred=classifier.predict(X_test)


# #### Accuracy

# In[32]:


from sklearn.metrics import classification_report


# In[36]:


print(classification_report(Y_test,y_pred))


# ## Convert the below Markdown to Code to find the accuracy on validation data 

# df_val = pd.read_csv('Cleaned_val_data.csv')
# 
# X_val = df_val.iloc[:,1:]
# Y_val = df_val.iloc[:,0]
# 
# X_val = X_val.replace('\;','',regex=True).astype(float)
# 
# X_val=sc.transform(X_val)
# 
# y_pred=classifier.predict(X_val)
# print(classification_report(y_val,y_pred))

# In[ ]:





# In[ ]:




