#!/usr/bin/env python
# coding: utf-8

# 
# Question 1
# 

# In[3]:


import pandas as pd
course_name = ["Data Science", "Machine Learning", "Big Data", "Data Engineer"]
duration = [2,3,6,4]
df = pd.DataFrame(data = {"course_name" : course_name, "duration" : duration})
df.iloc[1:2,:]


# Question 2

# The loc() function is label based data selecting method which means that we have to pass the name of the row or column which we want to select.
# The iloc() function is an indexed-based selecting method which means that we have to pass an integer index in the method to select a specific row/column.
# 

# Question 3

# In[4]:


new_df=df.reindex([3,0,1,2])
print(new_df.loc[2],"\n")
print(new_df.iloc[2])
#there is a difference in output,because loc takes name as index and iloc takes integer index


# Question 4

# In[5]:


import pandas as pd
import numpy as np
columns = ['column_1', 'column_2', 'column_3', 'column_4', 'column_5', 'column_6']
indices = [1,2,3,4,5,6]
#Creating a dataframe:
df1 = pd.DataFrame(np.random.rand(6,6), columns = columns, index = indices)
print("mean for every column:\n",df1.mean())
print("------------------")
print("standard ceviation of column_2:",df1["column_2"].std())


# Question 5

# In[7]:


df1['column_2']=df1['column_2'].apply(lambda x : str(x))
df1['column_2'].mean()
#getting error because mean can be calculated only for numerical data


# Question 6

# In[9]:


# windowing operations - an operation that performs an aggregation over a sliding partition of values.
### Types
# Rolling window
# Weighted window
# Expanding window
# Exponentially Weighted window


# Question 7

# In[10]:


print(pd.datetime.now())


# Question 8

# In[11]:


date1=pd.to_datetime(input())
date2=pd.to_datetime(input())
print(date2-date1)


# Question 9

# In[13]:


ex=pd.DataFrame({
    'id':[1,2,3,4,5,6],
    'Fruit':['ap','ba','or','ap','ba','or'],
    'sales':[5,2,4,7,9,2]
})
ex.to_csv('examples.csv')

file_path = input("Enter the file path: ")
column_name = input("Enter the column name: ")
category_order = input("Enter the category order (comma-separated): ").split(",")
df = pd.read_csv(file_path)
df[column_name] = pd.Categorical(df[column_name], categories=category_order, ordered=True)
df = df.sort_values(by=column_name)
df


# Question 10

# In[15]:


data=pd.DataFrame({
    'product':['apple','banana','cat','dog','elephant'],
    'sales':[10,56,42,96,12]
})
data.to_csv("sales.csv")
file_path = input("Enter the file path: ")
x_column_name = input("Enter the column name to plot in x-axis: ")
y_column_name = input("Enter the column name to plot in y- =axis: ")
df3=pd.read_csv(file_path)
df3.plot(kind="bar",x=x_column_name,y=y_column_name)


# Question 11

# In[16]:


student=pd.DataFrame({"stu_id":[1,2,3,4,5,6,7],"score":[99,83,87,52,35,83,54]})
student.to_csv("student.csv")
df4=pd.read_csv(input("Enter the file path: "))
print('+-----------+--------+')
print('| Mean | ',df4['score'].mean(),'|')
print('+-----------+--------+')
print('| Median |',df4['score'].median(),'|')
print('+-----------+--------+')
print('|Mode | ', df4['score'].mode(),'|')


# In[ ]:




