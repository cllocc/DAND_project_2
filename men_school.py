#!/usr/bin/env python
# coding: utf-8

# # Average Years In School Men Age 15-24
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# </ul>

# <a id='intro'></a>
# 
# <font color=#303F9F>This part of the project for "Investigating Country GDP and Education" will focus on the average years spent in school men aged 15 to 24. Choosing to investigage the top GDP/Capita countries above the mean.</font>
# <p>
# <li><font color=green>Luxembourg</li></font>
# <li><font color=blue>Norway</li></font>
# <li><font color=red>Denmark</li></font>
# <li><font color=gold>Sweden</li></font>
# <li><font color=#81D4FA>Australia</li></font>

# <a id='wrangling'></a>
# # Lets Do Some Wrangling and Oganizing.
# 
# <font color=#303F9F>We start by importing all of our necessary libraries and the data we want to analyze "mean_years_in_school_men_15_to_24_years.csv".</font>
# <p>
# <font color=#303F9F><li>Pandas to help us wrangle and organize our data</li></font>
# <font color=#303F9F><li>Matplotlib to create beautiful visualizations</li></font>
# <font color=#303F9F><li>Seaborn for visualization styling</li></font>
# <font color=#303F9F><li>Numpy to help with scientific computing</li></font>
# 

# In[15]:


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

#Average years in school Men aged 15-24
df_men = pd.read_csv('mean_years_in_school_men_15_to_24_years.csv')


# In[16]:


#Viewing the data from mean years in school men aged 15-24
df_men.head()


# <font color=#303F9F>You’ll notice the use of “.head()” quite extensively this is just for saving space.</font>

# In[17]:


#View the decribed data
df_men.describe()


# In[18]:


#view duplicate records
df_men.duplicated().sum()


# In[19]:


#Check null records
df_men.isnull().sum().head()


# <font color=#303F9F>We run into a problem with year being in the header. This makes it difficult to work with the data set. Luckily there is a function called “MELT” in the pandas library that will place all dates within a new column.</font>

# In[20]:


#using padas melt function to organize the data the way I want it
men_education = pd.melt(df_men, id_vars=['country'],var_name='year', value_name='education')
men_education.head()


# In[21]:


#Using the describe function we investigate our newly formed data
men_education.describe()


# In[22]:


#view records for samples & columns
men_education.shape


# In[23]:


#Check data types
men_education.dtypes


# In[24]:


#Check null records
men_education.isnull().sum().head()


# In[25]:


#view duplicate records
men_education.duplicated().sum()


# <a id='eda'></a>
# 
# <font color=#303F9F>Running queries for our desired countries we are able to create a line chart visualization. </font>
# <p>
# <li><font color=green>Luxembourg</li></font>
# <li><font color=blue>Norway</li></font>
# <li><font color=red>Denmark</li></font>
# <li><font color=gold>Sweden</li></font>
# <li><font color=#81D4FA>Australia</li></font>

# In[26]:


#Average years in school men age 15-24 query by high GDP/Capita Country
#se_edu_men = men_education.query('country.str.contains("Sweden")')
#au_edu_men = men_education.query('country.str.contains("Australia")')
#lux_edu_men = men_education.query('country.str.contains("Luxembourg")')
#no_edu_men = men_education.query('country.str.contains("Norway")')
#dk_edu_men = men_education.query('country.str.contains("Denmark")')

se_edu_men = men_education[men_education['country'].str.contains("Sweden")]
au_edu_men = men_education[men_education['country'].str.contains("Australia")]
lux_edu_men = men_education[men_education['country'].str.contains("Luxembourg")]
no_edu_men = men_education[men_education['country'].str.contains("Norway")]
dk_edu_men = men_education[men_education['country'].str.contains("Denmark")]

se_edu_men.head()


# <font color=#303F9F>Create a visual reprsentation </font>

# In[27]:


#Line plot for the countries selected.
def top_gdp_mschool():
    year = list(range(1970, 2016))
    se_edu = se_edu_men['education']
    au_edu = au_edu_men['education']
    lux_edu = lux_edu_men['education']
    no_edu = no_edu_men['education']
    dk_edu = dk_edu_men['education']

    plt.plot(year, au_edu, color='c', label='Australia')
    plt.plot(year, se_edu, color='y', label='Sweden')
    plt.plot(year, no_edu, color='b', label='Norway')
    plt.plot(year, dk_edu, color='r', label='Denmark')
    plt.plot(year, lux_edu, color='g', label='Luxembourg')
    
    plt.legend(loc='lower right')
    plt.xlabel('Year')
    plt.ylabel('Mean years in School')
    plt.title('Mean Years In School Men 15-24 ')
    return plt.show()

top_gdp_mschool()

