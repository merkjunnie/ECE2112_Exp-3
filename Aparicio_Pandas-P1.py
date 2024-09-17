#!/usr/bin/env python
# coding: utf-8

# # <b> Python Data Analysis (PANDAS) <b>
# ## _Programming Assessment 3A_

# #### _Access the Pandas Library using the import convention_

# In[66]:


import pandas as pd 


# ***

# ## <b> Data Manipulation: Displaying Specific Elements of the Table <b>

# ### <b>Problem 1.A.</b> &nbsp; Using knowledge obtained from the demonstrations, load the corresponding .csv file into a data frame named cars using pandas.

# #### _Output:_

# In[54]:


cars = pd.read_csv('cars.csv')
cars

# This loads the file "cars.csv" from the folder within the same directory and stores it to variable "cars


# ***

# ### <b>Problem 1.B.</b> &nbsp; Display the first five and last five rows of the resulting cars.

# #### _Output:_

# In[57]:


cars.head(5)

# .head() function displays only the first five rows of data in the table
# .head("number of rows") function is another way to display a specific number of rows from the beginning of your data


# In[59]:


cars.tail(5)

# .tail()" function displays only the last five rows of data in the table,
# .tail("number of rows") function is another way to display a specific number of rows from the end of your data


# ***
