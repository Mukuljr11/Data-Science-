#!/usr/bin/env python
# coding: utf-8

# # Mukul Sharma
# This is a Data Analysis Project related to a car dataset.
# Following is the project showing COMPARISON between different attributes of a car and the relation between them.

# # Importing the necessary libraries

# In[57]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# # Reading the Dataset 

# In[3]:


df=pd.read_csv('Automobile.csv')
df


# # Exploratory Data Analysis(EDA)

# In[4]:


df.head()


# In[5]:


df.shape


# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


df.describe(include='all')


# # Histogram

# In[9]:


sns.histplot(data=df, x='horsepower',bins=20)


# In[10]:


sns.histplot(data=df, x='horsepower',bins=2)


# # Histogram showing the relationship between the count of cars with respective horsepower.

# In[11]:


sns.histplot(data=df, x='horsepower',bins=10)


# In[12]:


sns.histplot(data=df, x='horsepower', kde=True)


# In[13]:


sns.histplot(data=df, x='weight', kde=True)


# In[14]:


df


# In[15]:


sns.histplot(data=df, x='acceleration', hue='cylinders', kde=True);


# In[16]:


g = sns.FacetGrid(df, col="cylinders")
g.map(sns.histplot, "acceleration");


# In[17]:


sns.boxplot(data=df, x='horsepower')


# In[18]:


sns.boxplot(data=df, x='cylinders', y='horsepower')


# # Boxplot showing the data and outliers for horsepower with respect to cylinders of the cars.

# # BarGraph

# In[19]:


sns.countplot(data=df, x='cylinders');


# # The above data shown is a barplot that describes the count of cars with certain cylinders.

# In[20]:


df


# In[21]:


sns.countplot(data=df, x='cylinders', hue='origin');


# In[22]:


plt.figure(figsize=(50,8))
sns.countplot(data=df,x='horsepower')
plt.show()


# In[23]:


sns.countplot(data=df,x='origin')


# In[24]:


plt.figure(figsize=(90,20))
sns.countplot(data=df, x='mpg')
plt.xticks(rotation=90)
plt.show()


# In[25]:


plt.title('Histogram: Cylinders')
plt.xlim(0,10)
plt.ylim(0,300)
plt.xlabel('Cylinders')
plt.ylabel('Frequency')
sns.histplot(data=df, x='cylinders', color='red');


# In[26]:


plt.title('Histogram: Acceleration')
plt.xlim(0,30)
plt.ylim(0,80)
plt.xlabel('Accceleration')
plt.ylabel('Frequency')
sns.histplot(data=df, x='acceleration', color='blue');


# In[27]:


df


# In[28]:


plt.figure(figsize=(10,7))
plt.title('Barplot: origin')
plt.ylim(0,150)
plt.xlabel('Origin')
sns.countplot(data=df, x='cylinders', hue='origin');


# # ScatterPlot

# In[29]:


sns.scatterplot(data=df, x='cylinders', y='horsepower');


# # In the above plot the data scattered is shown between the horsepower and the cylinders attributes. 

# In[30]:


sns.scatterplot(data=df,x='cylinders',y='weight')


# In[31]:


sns.scatterplot(data=df,x='cylinders',y='weight',hue='origin')


# # lmplot(linear model)

# In[32]:


sns.lmplot(data=df,x='weight',y='cylinders')


# In[33]:


sns.lmplot(data=df,x='weight',y='cylinders',hue='origin')


# In[34]:


sns.lmplot(data=df,x='weight',y='cylinders',col='origin')


# In[35]:


plt.figure(figsize=(10,7))
sns.stripplot(data=df, x='cylinders', y='weight', hue="origin", jitter=True);


# # ViolinPlot

# In[36]:


sns.violinplot(data=df, x='cylinders',y='horsepower',orient='v');


# # SwarmPlot

# In[37]:


sns.swarmplot(data=df, x='cylinders', y='horsepower');


# # Catplot

# In[38]:


sns.catplot(data=df, x='cylinders', y ='horsepower', hue='origin', kind='point');


# In[39]:


df


# # Heatmap

# In[40]:


sns.heatmap(data=df[['weight','cylinders','horsepower']].corr(),annot=True);


# # The relationship/co-relation between the 3 attributes that are 'weight', 'cylinders', and 'horsepower' is shown with the help of a heatmap.

# In[54]:


get_ipython().system('pip install plotly')


# In[58]:


import plotly.express as px


# In[59]:


pic= px.scatter_3d(df,x='cylinders',y='horsepower',z='acceleration',color='horsepower')
pic.show()


# # The above 3d plot shows the co-relation between the given attributes and tells us about how the three actually depend on each other.

# In[ ]:




