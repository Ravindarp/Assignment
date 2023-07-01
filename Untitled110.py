#!/usr/bin/env python
# coding: utf-8

# Q1. List any five functions of the pandas library with execution.
# 
# 

# In[2]:


#1)read_csv()
import pandas as pd
rr=pd.read_csv('services.csv')
print(rr)


# In[3]:


#2)head()
import pandas as pd
rr=pd.read_csv('services.csv')
print(rr.head())


# In[4]:


#3)tail()
import pandas as pd
rr=pd.read_csv('services.csv')
print(rr.tail())


# In[5]:


#4)describe()
import pandas as pd
rr=pd.read_csv('services.csv')
print(rr.describe())


# In[11]:


#5)mean()
import pandas as pd
rr=pd.read_csv('services.csv')
print((rr.mean()))


# Q2. Given a Pandas DataFrame df with columns 'A', 'B', and 'C', write a Python function to re-index the
# DataFrame with a new index that starts from 1 and increments by 2 for each row.

# In[10]:


import numpy as np
d={
    'A':[11,12,13],
    'B':[21,22,23],
    'C':[31,32,33]
}
df1=pd.DataFrame(d)
df1.reindex([1,3],fill_value=0)


# Q3. You have a Pandas DataFrame df with a column named 'Values'. Write a Python function that
# iterates over the DataFrame and calculates the sum of the first three values in the 'Values' column. The
# function should print the sum to the console.
# For example, if the 'Values' column of df contains the values [10, 20, 30, 40, 50], your function should
# calculate and print the sum of the first three values, which is 60.

# In[17]:


d={
    'values':[1,2,3,6,5,4,7,8]
}
df=pd.DataFrame(d)
print(df)
t=0
s=0
for i in df.iterrows():
    if t<4:
        t+=1
        s+=i[0]
print("the sum of first three elements is:",s)



# Q4. Given a Pandas DataFrame df with a column 'Text', write a Python function to create a new column
# 'Word_Count' that contains the number of words in each row of the 'Text' column.

# In[21]:


d={
    'text':['hello there i am ravi ','how are you?','this is data science masters','did you check on me']
}
df=pd.DataFrame(d)
df["word_count"]=df["text"].apply(lambda x : len(x.split(" ")))
df


# Q5. How are DataFrame.size() and DataFrame.shape() different?
# 
# 

# DataFrame.size() and DataFrame.shape() are both are attributes in pandas 
# DataFrame.size() is used to give the number of elements in the DataFrame 
# DataFrame.shape() is used to tell number of dimensions in DataFrame
# 
# 

# Q6. Which function of pandas do we use to read an excel file?
# 
# 

# read_excel()  function of pandas we use to read an excel file?
# 
# 

# Q7. You have a Pandas DataFrame df that contains a column named 'Email' that contains email
# addresses in the format 'username@domain.com'. Write a Python function that creates a new column
# 'Username' in df that contains only the username part of each email address.
# The username is the part of the email address that appears before the '@' symbol. For example, if the
# email address is 'john.doe@example.com', the 'Username' column should contain 'john.doe'. Your
# function should extract the username from each email address and store it in the new 'Username'
# column.
# 

# In[27]:


import pandas as pd
data= {
    'Email': ['john.doe@example.com', 'jane.smith@example.com', 'adam.wilson@example.com']
}
df=pd.DataFrame(data)
def eu(df):
    df['username']=df['Email'].str.split('@').str[0]
    return  df
y=eu(df)
print(y)


# Q8. You have a Pandas DataFrame df with columns 'A', 'B', and 'C'. Write a Python function that selects
# all rows where the value in column 'A' is greater than 5 and the value in column 'B' is less than 10. The
# function should return a new DataFrame that contains only the selected rows.
# For example, if df contains the following values:
# A B C
# 0 3 5 1
# 1 8 2 7
# 2 6 9 4
# 3 2 3 5
# 4 9 1 2
# Your function should select the following rows: A B C
# 1 8 2 7
# 4 9 1 2
# The function should return a new DataFrame that contains only the selected rows.
# 
# 

# In[31]:


import pandas as pd
data={
    'A':[3,8,6,2,9],
    'B': [5, 2, 9, 3, 1],
    'C': [1, 7, 4, 5, 2]
    
}
df=pd.DataFrame(data)
def ss(df):
    rr=df[(df['A']>5) & (df['B']<10)]
    return rr
rt=ss(df)
print(rt)


# Q9. Given a Pandas DataFrame df with a column 'Values', write a Python function to calculate the mean,
# median, and standard deviation of the values in the 'Values' column.
# 
# 

# In[37]:


import pandas as pd

data = {
    'Values': [7, 9, 12, 6, 15, 8, 10]
}
df = pd.DataFrame(data)
def cs(df):
    mean=df['Values'].mean()
    median=df['Values'].median()
    std=df['Values'].std()
    return mean,median,std
mean,median,std=cs(df)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std)


# Q10. Given a Pandas DataFrame df with a column 'Sales' and a column 'Date', write a Python function to
# create a new column 'MovingAverage' that contains the moving average of the sales for the past 7 days
# for each row in the DataFrame. The moving average should be calculated using a window of size 7 and
# should include the current day.

# In[42]:


import pandas as pd
data = {
    'Date': ['2023-06-25', '2023-06-26', '2023-06-27', '2023-06-28', '2023-06-29', '2023-06-30', '2023-07-01'],
    'Sales': [100, 150, 200, 175, 250, 300, 225]
}
df = pd.DataFrame(data)
def calculate_moving_average(df):
    df['MovingAverage']=df['Sales'].rolling(window=7,min_periods=1).mean()
    return df
df=calculate_moving_average(df)
print(df)


# Q11. You have a Pandas DataFrame df with a column 'Date'. Write a Python function that creates a new
# column 'Weekday' in the DataFrame. The 'Weekday' column should contain the weekday name (e.g.
# Monday, Tuesday) corresponding to each date in the 'Date' column.
# For example, if df contains the following values:
# Date
# 0 2023-01-01
# 1 2023-01-02
# 2 2023-01-03
# 3 2023-01-04
# 4 2023-01-05
# Your function should create the following DataFrame:
# 
# Date Weekday
# 0 2023-01-01 Sunday
# 1 2023-01-02 Monday
# 2 2023-01-03 Tuesday
# 3 2023-01-04 Wednesday
# 4 2023-01-05 Thursday
# The function should return the modified DataFrame.

# In[52]:


import pandas as pd
df = pd.DataFrame({'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05']})
def add_weekday(df):
    df['Weekday']=pd.to_datetime(df['Date']).dt.day_name()
    return df
df = add_weekday(df)
print(df)


# Q12. Given a Pandas DataFrame df with a column 'Date' that contains timestamps, write a Python
# function to select all rows where the date is between '2023-01-01' and '2023-01-31'.

# In[5]:


import pandas as pd
def select_rows_between_dates(df):
    df['Date']=pd.to_datetime(df['Date'])
    start_date = pd.to_datetime('2023-01-01')
    end_date = pd.to_datetime('2023-01-31')
    mask=(df['Date']>=start_date) & (df['Date']<=end_date)
    selected_rows=df[mask]
    return selected_rows
df = pd.DataFrame({'Date': ['2023-01-01', '2023-01-15', '2023-02-01', '2023-01-25']})
selected_rows = select_rows_between_dates(df)

# Print the selected rows
print(selected_rows)


# Q13. To use the basic functions of pandas, what is the first and foremost necessary library that needs to
# be imported?

#  To use the basic functions of pandas  first and foremost necessary library that needs to be imported is "pandas" library

# In[ ]:




