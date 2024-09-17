#!/usr/bin/env python
# coding: utf-8

# # <b> Python Data Analysis (PANDAS) </b>
# ## _Programming Assessment 3B_

# #### Access the Pandas Library using the import convention

# In[7]:


import pandas as pd


# ***

# ## <b> Data Manipulation: Subsetting, Slicing, and Indexing Applications <b>

# #### In this part, we will be able to extract the following information from "cars" dataframe and perform using subsetting, slicing and indexing operations on PANDAS.

# #### Data _(stored on variable "cars")_:

# In[14]:


# Extract the data from the cars file and store it to variable "cars"

cars = pd.read_csv('cars.csv')
cars


# ***

# ### <b> Problem 2.A. </b> &nbsp; Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of car

# #### _Analysis:_

# > In <b>slicing</b>, the `.iloc` function in PANDAS is used to access a group of rows and columns based on their specific positions. Since <b> dataframes follow zero-based indexing</b>, the goal is this problem to display the data within rows 0 to 4 and also display only those columns that represent as an odd number starting from "Model" to "Carl".

# #### _Output:_

# In[16]:


cars.iloc[:5, ::2]


# #### _Explanation:_

# > I used the .iloc function to display a group of rows and columns in terms of their numerical position. `:5` with respect to zero-based indexing, includes only from 0 to 4 (5 is not included). Lastly, `::2` indicates that every second column, starting from the first, should be selected. This effectively picks columns 1,3,5, etc., which are the "odd-numbered columns in zero-based indexing.

# ***

# ### <b> Problem 2.B. </b> &nbsp; Display the row that contains the ‘Model’ of ‘Mazda RX4'.

# #### _Analysis:_

# > In <b>indexing</b>, the `.loc` function in PANDAS is also
# used to access a group of rows and columns using a <b>specified condition</b>. In this problem, the goal is to display the row where the model "Mazda RX4" is located. From that, we can create a condition that only searches for "Mazda RX4" within the 'Model' column and displays all the row elements where "Mazda RX4" belongs.

# #### _Output:_

# In[192]:


cars.loc[cars['Model'] == 'Mazda RX4'] 


# #### _Explanation:_

# > I used the .loc function through indexing to access a specific row where "Mazda RX4" is located and displays all the column elements of that row. By performing a conditional statement, `cars['Model'] == 'Mazda RX4'`, this only searches for 'Mazda RX4' within the 'Model' column. Lastly, since there is no other condition that might change how many column elements within that row will be displayed, all elements are displayed instead.

# ***

# ### <b> Problem 2.C. </b> &nbsp; How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

# #### _Analysis:_

# > This problem can be solved using the `.iloc` function. In subsetting, you extract a single or set of elements from a data table <b>with optimized codes</b>. Since we are asked to find how many cylinders cyl’ the car model ‘Camaro Z28’ has, it tells us to find and extract a set of elements from only the rows where the car model matches 'Camaro Z28'.

# #### _Output:_

# In[267]:


cars.iloc[[23], [0,2]]


# #### _Explanation:_

# > I used the ".iloc function" to extract specific elements from the row of 'Camaro Z28'. `[23]` specifies the location of 'Camaro Z28' in line with the rows. On the other hand, `[0,2]` specifies the location of the column elements that I want to access from that row which returned an output of an element within 'Model' and 'cyl'.

# ***

# ### <b> Problem 2.D. </b> &nbsp; Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
# 

# #### _Analysis:_

# > This problem can also be solved using the `.iloc` function through subsetting where we extract elements from only the rows where the car model matches the specified car models from the problem and display only their information in the 'Model', 'cyl', and 'gear' column.

# #### _Output:_

# In[338]:


cars.iloc[[1, 18, 28], [0,2]]


# #### _Explanation:_

# > Similarly with the explanation in Problem 2.C., I used the ".iloc function" to extract specific elements from the rows of car models (Mazda RX4 Wag, Ford Pantera L, and Honda Civic). `[1, 18, 28]` specifies the positions of such models in line with the rows and `[0, 2]` specifies the location of the column elements that I want to access from the inputted rows

# ***

# In[9]:


pd.save('Aparicio_Pandas-P1.npy', cars)


# In[ ]:




