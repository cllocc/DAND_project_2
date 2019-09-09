#!/usr/bin/env python
# coding: utf-8

# # GDP Percentage Based On Total Indusrty
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# </ul>

# <a id='intro'></a>
# 
# <font color=#303F9F>This part of the project for "Investigating Country GDP and Education" will focus on the total percentage of industry for each year 1960-2017. Choosing to investigage the top GDP/Capita countries above the mean.</font>
# <p>
# <li><font color=green>Luxembourg</li></font>
# <li><font color=blue>Norway</li></font>
# <li><font color=red>Denmark</li></font>
# <li><font color=gold>Sweden</li></font>
# <li><font color=#81D4FA>Australia</li></font>

# <a id='wrangling'></a>
# # Lets Do Some Wrangling and Oganizing. YEEEEEHaw
# 
# <font color=#303F9F>We start by importing all of our necessary libraries and the data we want to analyze "industry_percent_of_gdp.csv".</font>
# <p>
# <font color=#303F9F><li>Pandas to help us wrangle and organize our data</li></font>
# <font color=#303F9F><li>Matplotlib to create beautiful visualizations</li></font>
# <font color=#303F9F><li>Seaborn for visualization styling</li></font>
# <font color=#303F9F><li>Numpy to help with scientific computing</li></font>
# 

# In[15]:


#Import Packages and read the data
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')

#Set Chartting Style
sns.set(style="whitegrid")

#Setting figure size for visuals
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 10
fig_size[1] = 6

#GDP Percent Idustry by county & year 1970-2017 
gdp_industry = pd.read_csv('industry_percent_of_gdp.csv')

#Viewing GDP Industry Data
gdp_industry.head()


# <font color=#303F9F>You’ll notice the use of “.head()” quite extensively this is just for saving space.</font>

# In[16]:


#Investigate the data 189 Row & 59 Columns
gdp_industry.shape


# In[17]:


#Investigate the data types we don't want an INT or Float to be a String.
gdp_industry.dtypes.head()


# In[18]:


#Investigate null records
gdp_industry.isnull().sum().head()


# In[19]:


#Investigate duplicate records
gdp_industry.duplicated().sum()


# In[20]:


#Investigate number of unique values in each column
gdp_industry.nunique().head()


# In[21]:


#Generate descriptive statistics that summarize the central tendency, dispersion and shape of a dataset’s distribution.
gdp_industry.describe()


# <font color=#303F9F>We run into a problem with year being in the header. This makes it difficult to work with the data set. Luckily there is a function called “MELT” in the pandas library that will place all dates within a new column.</font>

# In[22]:


#using padas melt function to organize and relable the data. The year being in the header to the year being a column.
gdp_industry_cleaner = pd.melt(gdp_industry, id_vars=['country'],var_name='year', value_name='gdp')
gdp_industry_cleaner.head()


# In[23]:


gdp_industry_cleaner.dtypes
gdp_industry_cleaner['year'] = gdp_industry_cleaner['year'].astype(int)
gdp_industry_cleaner.dtypes


# <a id='eda'></a>
# 
# <font color=#303F9F>Running queries for our desired countries we are able to create a line chart visualization. </font>
# <p>
# <li><font color=green>Luxembourg</li></font>
# <li><font color=blue>Norway</li></font>
# <li><font color=red>Denmark</li></font>
# <li><font color=gold>Sweden</li></font>
# <li><font color=#81D4FA>Australia</li></font>

# In[24]:


#Query the desired countries Python 3.7/pandas updated
#lu = gdp_industry_cleaner.query('country.str.contains("Luxembourg")')
#no = gdp_industry_cleaner.query('country.str.contains("Norway")')
#dk = gdp_industry_cleaner.query('country.str.contains("Denmark")')
#se = gdp_industry_cleaner.query('country.str.contains("Sweden")')
#au = gdp_industry_cleaner.query('country.str.contains("Australia")')

#Query the desired countries
lu = gdp_industry_cleaner[gdp_industry_cleaner['country'].str.contains("Luxembourg")]
no = gdp_industry_cleaner[gdp_industry_cleaner['country'].str.contains("Norway")]
dk = gdp_industry_cleaner[gdp_industry_cleaner['country'].str.contains("Denmark")]
se = gdp_industry_cleaner[gdp_industry_cleaner['country'].str.contains("Sweden")]
au = gdp_industry_cleaner[gdp_industry_cleaner['country'].str.contains("Australia")]


# <font color=#303F9F>Create A Line Chart </font>

# In[25]:


#Line Chart For GDP % Industry 1970-2017
def gdp_industry_line_chart():
    
    sns.set(style="whitegrid")
    year = list(range(1960, 2018))
    lu_gdp = lu['gdp']
    no_gdp = no['gdp']
    dk_gdp = dk['gdp']
    se_gdp = se['gdp']
    au_gdp = au['gdp']

    plt.plot(year, lu_gdp, color='g', label='Luxembourg')
    plt.plot(year, no_gdp, color='b', label='Norway')
    plt.plot(year, dk_gdp, color='r', label='Denmark')
    plt.plot(year, se_gdp, color='y', label='Sweden')
    plt.plot(year, au_gdp, color='c', label='Australia')

    plt.legend(loc='upper left')
    plt.xlabel('Year')
    plt.ylabel('Percentage of GDP')
    plt.title('Overall Percentage of GDP in Industry')
    return plt.show()

gdp_industry_line_chart()


# <font color=#303F9F>Lets take a look at Norway based on a box plot. The reason for doing this is because we have extensive data. It is also interesting that from 1970 to 2017 Norway has increased as an industrial nation. All other nations have been on the decline.</font>

# In[26]:


def gdp_percent_industry_norway_box():
    
    #lu.plot.box(x= 'year', y= 'gdp', title= 'Luxembourg Industry GDP Box Plot');
    no.plot.box(x= 'year', y= 'gdp', title= 'Norway Overall Industry GDP 1970-2017 Box Plot',patch_artist=True, label='Norway')
    plt.legend(no.country.iloc[0:1])
    plt.ylabel('Percentage Of GDP')
    return plt.show()
    #dk.plot.box(x= 'year', y= 'gdp', title= 'Denmark Industry GDP Box Plot');
    #se.plot.box(x= 'year', y= 'gdp', title= 'Sweden Industry GDP Box Plot');
    #au.plot.box(x= 'year', y= 'gdp', title= 'Australia Industry GDP Box Plot');
    
gdp_percent_industry_norway_box();


# In[27]:


no.country.iloc[0:1]

