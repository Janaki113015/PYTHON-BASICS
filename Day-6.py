#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[5]:


df=pd.read_csv('age.CSV')


# In[6]:


df.head()


# In[15]:


import pandas as pd

# Define the path to your CSV file
df=pd.read_csv(r'C:\Users\Janaki\OneDrive\Desktop\age.csv')
print(df.head(15))
print(df.head())


# In[13]:


import matplotlib.pyplot as plt

# Scatter plot of Age vs Purchased
plt.figure(figsize=(5, 4))
plt.scatter(df['Age'], df['Purchased'], cmap='bwr', label='Purchased') 
plt.xlabel('Age')
plt.ylabel('Purchased (0 = No, 1 = Yes)')
plt.title('Abhi Project')
plt.legend(['No Purchase', 'Purchase'])  
plt.grid(True)  
plt.show()  


# In[31]:


from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
#features and target variable
X=df[['Age']]
Y=df[['Purchased']]
#split the data into
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
model=LogisticRegression()
model.fit(X_train,Y_train)
#predicition
new_age=[[59]]
prediction=model.predict(new_age)
probability=model.predict_proba(new_age)
print(f"prediction for Age {new_age[0][0]}: {'Will purchase' if prediction[0]==1 else 'will not purchase' }")
print(f"Probability: {probability[0]}")


# In[ ]:




