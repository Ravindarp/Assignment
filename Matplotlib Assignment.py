#!/usr/bin/env python
# coding: utf-8

# Question 1
# 

# Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. Matplotlib makes easy things easy and hard things possible. Create publication quality plots. Make interactive figures that can zoom, pan, update.
# 
# five plots that can be plotted using the Pyplot module of Matplotlib are:
# 
# barplot
# scatterplot
# barplot
# histogram
# pie chart
# 

# Question 2
# 

# A scatter plot is a type of graph that uses Cartesian coordinates to display the relationship between two variables. It is useful for visually representing the correlation or relationship between two numerical variables, where one variable is plotted on the x-axis and the other variable is plotted on the y-axis.
# 
# Each point on the plot represents a unique combination of the two variables. The position of each point on the plot indicates the value of the corresponding values of the two variables.
# 
# 

# In[5]:


import matplotlib.pyplot as plt
import numpy as np
np.random.seed(3)
x = 3 + np.random.normal(0, 2, 50)
y = 3 + np.random.normal(0, 2, len(x))
plt.scatter(x,y,c="magenta",alpha=0.5)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("scatter plot")
plt.show()


# Question 3

# The subplot() function in Matplotlib is used to create multiple plots in a single figure. It takes three arguments - the number of rows, the number of columns, and the plot number, and returns a handle to the corresponding subplot.
# 
# 

# In[19]:


x1 = np.array([0, 1, 2, 3, 4, 5])
y1 = np.array([0, 100, 200, 300, 400, 500])

x2 = np.array([0, 1, 2, 3, 4, 5])
y2 = np.array([50, 20, 40, 20, 60, 70])

x3 = np.array([0, 1, 2, 3, 4, 5])
y3 = np.array([10, 20, 30, 40, 50, 60])

x4 = np.array([0, 1, 2, 3, 4, 5])
y4 = np.array([200, 350, 250, 550, 450, 150])

plt.figure()
plt.subplot(2,2,1)
plt.plot(x1,y1)
plt.subplot(2,2,2)
plt.plot(x2,y2)
plt.subplot(2,2,3)
plt.plot(x3,y3)
plt.subplot(2,2,4)
plt.plot(x4,y4)
plt.show()


# Question 4

# A bar plot is a type of plot that displays data using rectangular bars. The height or length of each bar represents the value of a particular variable, while the width of the bar remains constant. Bar plots are used to compare different values of a variable or to show the distribution of a variable across categories.

# In[20]:


import numpy as np
company = np.array(["Apple", "Microsoft", "Google", "AMD"])
profit = np.array([3000, 8000, 1000, 10000])
plt.bar(company,profit,color="cyan",alpha=0.5)
plt.title("Company Profits")
plt.xlabel("Company")
plt.ylabel("Profit (in millions)")
plt.show()


# Question 5

# A box plot, also known as a box-and-whisker plot, is a graphical representation of a dataset that summarizes the distribution of the data. It is used to show the median, quartiles, and outliers of the dataset.
# 
# The box in the plot represents the middle 50% of the data, where the bottom and top of the box represent the 25th and 75th percentiles, respectively. The line inside the box represents the median of the data. The whiskers extending from the box represent the range of the data, with the endpoints of the whiskers representing the minimum and maximum values. Outliers are plotted as individual points beyond the whiskers.
# 
# 

# In[22]:


box1 = np.random.normal(100, 10, 200)
box2 = np.random.normal(90, 20, 200)
fig, ax = plt.subplots()
ax.boxplot([box1,box2])
ax.set_xticklabels(['Box 1', 'Box 2'])
ax.set_ylabel('Value')
ax.set_title('Box Plot Example')
plt.show()


# In[ ]:




