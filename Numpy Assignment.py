#!/usr/bin/env python
# coding: utf-8

# Question 1
# 

# Yes, there is a difference in the data type of Python lists, arrays, and NumPy arrays.
# 
# list_ is a Python lists that can contain elements of different data types, and their size can be changed dynamically.
# 
# array_list is a NumPy arrays that are homogeneous collections of elements of the same data type but offer more functionalities and optimizations compared to arrays in Python. They can be created using the numpy module in Python.
# 
# 

# In[4]:


import numpy as np
list_ = ["1","2","3","4","5"]
array_list = np.array(object = list_)

print(type(list_))
print(type(array_list))


# In[ ]:


Question 2


# In[5]:


for element in list_:
    print(type(element))

print("********************")
for element in array_list:
    print(type(element))


# Question 3

# Yes, there will be a difference in the data type of the elements present in both the variables 'list_' and 'array_list'.
# 
# Before converting the list to a numpy array, the elements in the list were strings, and after converting to a numpy array with the default data type, the elements in the numpy array were also strings.
# 
# However, when the 'dtype' parameter was specified as 'int' during the creation of the numpy array, the elements in the numpy array were converted from strings to integers.
# 
# 

# In[8]:


array_list = np.array(object=list_,dtype=int)
print("Data type of elements in list_:", [type(x) for x in list_])
print("Data type of elements in array_list (after conversion):", array_list.dtype)


# Question 4

# In[9]:


import numpy as np
num_list = [ [ 1 , 2 , 3 ] , [ 4 , 5 , 6 ] ]
num_array = np.array(object = num_list)

print("the shape of num_list is :",np.shape(num_list))
print("the size of num_list is :",np.size(num_list))
print("----------------------------------------------")
print("the shape of num_array is :",np.shape(num_array))
print("the size of num_array is :",np.size(num_array))


# Question 5

# In[10]:


matrix=np.zeros((3,3))
print(matrix)


# Question 6

# In[11]:


ide=np.eye(5)
print(ide)


# In[ ]:




