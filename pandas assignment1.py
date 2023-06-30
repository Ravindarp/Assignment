#!/usr/bin/env python
# coding: utf-8

# Q1)Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, and 42. Then, print the series.

# In[3]:


import pandas as pd
data = [4, 8, 15, 16, 23, 42]
series=pd.Series(data)
print(series)


# Q2. Create a variable of list type containing 10 elements in it, and apply pandas.Series function on the
# variable print it.

# In[4]:


import pandas as pd
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data=pd.Series(my_list)
print(data)


# Q3. Create a Pandas DataFrame that contains the following data:
# Name
# Alice
# Bob
# Claire
# 
# Age
# 25
# 30
# 27
# 
# Gender
# Female
# Male
# Female
# Then, print the DataFrame.

# In[6]:


import pandas as pd
rr={"Name":['Alice','Bob','Claire'],
   'Age':[25,30,37],
   'Gender':['Female','Male','Female']}
tt=pd.DataFrame(rr)
print(tt)


# Q4. What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example.

# In[7]:


#DataFrame:It contists of rows and columns.It's also known as collection of 
#          series
#Series:It represent of columns data
#Eg for DataFrame
import pandas as pd
rr={"Name":['Alice','Bob','Claire'],
   'Age':[25,30,37],
   'Gender':['Female','Male','Female']}
tt=pd.DataFrame(rr)
print(tt)
#Eg for series
import pandas as pd
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data=pd.Series(my_list)
print(data)


# Q5. What are some common functions you can use to manipulate data in a Pandas DataFrame? Can
# you give an example of when you might use one of these functions?
# 
# 

# In[14]:


#head():head function used to display few elements in first row
#tail():tail function used to display few elements in last row
#drop():drop function used to remove rows or columns
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Claire'],
    'Age': [25, 30, 27],
    'Gender': ['Female', 'Male', 'Female']
}
df = pd.DataFrame(data)
print("First few rows of the DataFrame:")
print(df.head(1))
print('last few elements of dataframe:')
print(df.tail(1))
df_dropped = df.drop('Gender', axis=1)
print(df_dropped)


# Q6. Which of the following is mutable in nature Series, DataFrame, Panel?

# In pandas, both Series and DataFrame are mutable in nature, meaning they can be modified after creation. On the other hand, Panel is an immutable data structure, which means it cannot be modified once created.
# 
# 

# Q7. Create a DataFrame using multiple Series. Explain with an example.
# 

# In[15]:


import pandas as pd

name_series = pd.Series(['Alice', 'Bob', 'Claire'])
age_series = pd.Series([25, 30, 27])
gender_series = pd.Series(['Female', 'Male', 'Female'])

data = {
    'Name': name_series,
    'Age': age_series,
    'Gender': gender_series
}
df = pd.DataFrame(data)

print(df)


# In[ ]:




