#!/usr/bin/env python
# coding: utf-8

# # Average Years In School Women Age 15-24
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# </ul>

# <a id='intro'></a>
# 
# <font color=#303F9F>This part of the project for "Investigating Country GDP and Education" will focus on the average years spent in school women aged 15 to 24. Choosing to investigage the top GDP/Capita countries above the mean.</font>
# <p>
# <li><font color=green>Luxembourg</li></font>
# <li><font color=blue>Norway</li></font>
# <li><font color=red>Denmark</li></font>
# <li><font color=gold>Sweden</li></font>
# <li><font color=#81D4FA>Australia</li></font>

# <a id='wrangling'></a>
# # Lets Do Some Wrangling and Oganizing.
# 
# <font color=#303F9F>We start by importing all of our necessary libraries and the data we want to analyze "mean_years_in_school_women_15_to_24_years.csv".</font>
# <p>
# <font color=#303F9F><li>Pandas to help us wrangle and organize our data</li></font>
# <font color=#303F9F><li>Matplotlib to create beautiful visualizations</li></font>
# <font color=#303F9F><li>Seaborn for visualization styling</li></font>
# <font color=#303F9F><li>Numpy to help with scientific computing</li></font>
# 

# In[43]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

#Set Chartting Style
sns.set(style="whitegrid")

#Setting figure size for visuals
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 12
fig_size[1] = 9

#Average years in school women aged 15-24
df_women = pd.read_csv('mean_years_in_school_women_15_to_24_years.csv')


# In[44]:


#Viewing the data from mean years in school Women aged 15-24
df_women.head()


# <font color=#303F9F>You’ll notice the use of “.head()” quite extensively this is just for saving space.</font>

# In[45]:


#view records for samples & columns
df_women.shape


# In[46]:


#view duplicate records
df_women.duplicated().sum()


# In[47]:


#Check null records
df_women.isnull().sum().head()


# <font color=#303F9F>We run into a problem with year being in the header. This makes it difficult to work with the data set. Luckily there is a function called “MELT” in the pandas library that will place all dates within a new column.</font>
# 

# In[48]:


#using padas melt function to organize the data the way I want it
women_education = pd.melt(df_women, id_vars=['country'],var_name='year', value_name='education')
women_education.head()


# In[49]:


#exploring the newly formed data
women_education.describe()


# In[50]:


#view records for samples & columns
women_education.shape


# In[51]:


#Check data types
women_education.dtypes


# In[52]:


#Check null records
women_education.isnull().sum().head()


# In[53]:


#view duplicate records
women_education.duplicated().sum()


# <a id='eda'></a>
# 
# <font color=#303F9F>Running queries for our desired countries we are able to create a line chart visualization. </font>
# <p>
# <li><font color=green>Luxembourg</li></font>
# <li><font color=blue>Norway</li></font>
# <li><font color=red>Denmark</li></font>
# <li><font color=gold>Sweden</li></font>
# <li><font color=#81D4FA>Australia</li></font>

# In[54]:


#Average years in school Women age 15-24 query in relation to GDP data
#se_edu_women = women_education.query('country.str.contains("Sweden")')
#au_edu_women = women_education.query('country.str.contains("Australia")')
#lux_edu_women = women_education.query('country.str.contains("Luxembourg")')
#no_edu_women = women_education.query('country.str.contains("Norway")')
#dk_edu_women = women_education.query('country.str.contains("Denmark")')

se_edu_women = women_education[women_education['country'].str.contains("Sweden")]
au_edu_women = women_education[women_education['country'].str.contains("Australia")]
lux_edu_women = women_education[women_education['country'].str.contains("Luxembourg")]
no_edu_women = women_education[women_education['country'].str.contains("Norway")]
dk_edu_women = women_education[women_education['country'].str.contains("Denmark")]


# <font color=#303F9F>Create a visual reprsentation </font>

# In[55]:


#Line plot for the countries selected.
def top_gdp_wschool():
    year = list(range(1970, 2016))
    se_edu = se_edu_women['education']
    au_edu = au_edu_women['education']
    lux_edu = lux_edu_women['education']
    no_edu = no_edu_women['education']
    dk_edu = dk_edu_women['education']

    plt.plot(year, au_edu, color='c', label='Australia')
    plt.plot(year, se_edu, color='y', label='Sweden')
    plt.plot(year, no_edu, color='b', label='Norway')
    plt.plot(year, dk_edu, color='r', label='Denmark')
    plt.plot(year, lux_edu, color='g', label='Luxembourg')
    
    plt.legend(loc='upper left')
    plt.xlabel('Year')
    plt.ylabel('Mean years in School')
    plt.title('Mean years In School Women 15-24 ')
    return plt.show()

top_gdp_wschool()

