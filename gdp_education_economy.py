#!/usr/bin/env python
# coding: utf-8

# # Global GDP & Education Data Analysis
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>

# <a id='intro'></a>
# ## Investigating Global GDP & Education
# 
# <font color=#303F9F>Investigating our first data sheet “GDP/Capita USD Inflation Adjusted” We seek to understand which countries have the highest GDP/Capita for 2017. We also rank the top 5 countries for 2017 that are above the mean. Followed by questions regarding education and GDP.
# 
# Datasets Included Are as Followed:
# 
# 1.	gdppercapita_us_inflation_adjusted.csv (GDP/Capita USD Inflation Adjusted)
# 2.	industry_percent_of_gdp.csv (Overall percentage of GDP/Year Industry)
# 3.	services_percent_of_gdp.csv (Overall percentage of GDP/Year Industry)
# 4.	mean_years_in_school_men_15_to_24_years.csv (Mean years in school Men 15-24)
# 5.	mean_years_in_school_women_15_to_24_years.csv (Mean years in school Women 15-24)
# 
# Question:
# 
# <a href="#q1">1.	What are the top 5 highest GDP/Capita countries above the mean in 2017?</a>
# <p>
# <a href="#q2">2.	From the top 5 GDP/Capita countries in 2017, on average which countries stay in school longer? comparing  Men and Women between the ages of 15-24</a>
# <p>
# <a href="#q3">3.  Are these Countries predominantly a service or industrial based economy?</a>
# <p>
# <a href="#q4">4.	For service and industry is there an increase or decrease in these secotors?</a>
# <p>
# <a href="#q5">5.	Is Norway a balanced economy between its services and industrial sectors?</a></font>

# <a id='wrangling'></a>
# ## Lets Do Some Wrangling and Oganizing.
# 
# <font color=#303F9F>We start by importing all of our necessary libraries and the data we want to analyze "gdppercapita_us_inflation_adjusted.csv".</font>
# <p>
# <font color=#303F9F><li>Pandas to help us wrangle and organize our data</li></font>
# <font color=#303F9F><li>Matplotlib to create beautiful visualizations</li></font>
# <font color=#303F9F><li>Seaborn for visualization styling</li></font>
# <font color=#303F9F><li>Numpy to help with scientific computing</li></font>
# 

# In[19]:


#Import Packages and read the data

#Parts Of project
import industry_gdp
import services_gdp
import men_school
import women_school

#Wrangling and visualizing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')

#Set Chartting Style
sns.set(style="whitegrid")

#Setting figure size for visuals
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 10
fig_size[1] = 6

#GDP/Capita by county USD Inflation Adjusted 1970-2017 
df_gdp = pd.read_csv('gdppercapita_us_inflation_adjusted.csv')

#Viewing GDP Data
df_gdp.head()


# In[20]:


#Investigate our first data set that we will explore GDP Per Capita USD Inflation Adjusted, records for samples & columns
df_gdp.shape


# In[21]:


#Investigate Our Data Types GDP Per Capita US Inflation Adjusted
df_gdp.dtypes.head()


# In[22]:


#Investigate null records GDP Per Capita US Inflation Adjusted
df_gdp.isnull().sum().head()


# In[23]:


#Investigate duplicate records GDP Per Capita US Inflation Adjusted
df_gdp.duplicated().sum()


# In[24]:


#Investigate number of unique values in each column GDP Per Capita US Inflation Adjusted
df_gdp.nunique().head()


# In[25]:


#Generate descriptive statistics that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding NaN values.
df_gdp.describe()


# In[26]:


#Noticing there are null values in the data we drop the null values. We can analize the max rang of data without missing data when comparing different rows
df_gdp_alldata = df_gdp.dropna()
df_gdp_alldata.tail()


# <font color=#303F9F>We run into a problem with year being in the header. This makes it difficult to work with the data set. Luckily there is a function called “MELT” in the pandas library that will place all dates within a new column.</font>

# In[27]:


#using padas melt function to organize and relable the data. The year being in the header to the year being a column.
gdp_cleaner = pd.melt(df_gdp_alldata, id_vars=['country'],var_name='year', value_name='gdp')
gdp_cleaner.head()


# In[28]:


#Exploring the data again once it's cleaned
gdp_cleaner.describe()


# <a id='eda'></a>
# ## Exploratory Data Analysis

# <a id='q1'></a>
# ## Question 1:
# 
# <font color=#303F9F>What countries rank highest in GDP above the global average for 2017?</font>

# In[29]:


#Find GDP for countries for the year 2017 and describe
gdp_year_2017 = gdp_cleaner.query('year.str.contains("2017")')
gdp_year_2017.describe()


# In[30]:


#query to build list of countries with above mean GDP for 2017
gdp_above_avg_2017 = gdp_year_2017[gdp_year_2017['gdp'] >= 15571.770115]
highest_gdp_avg_2017 = gdp_year_2017.sort_values(by=['gdp'], ascending=False)
highest_gdp_avg_2017.head()


# In[31]:


#Higest GDP above global Mean top 5
lu = gdp_cleaner.query('country.str.contains("Luxembourg")')
no = gdp_cleaner.query('country.str.contains("Norway")')
dk = gdp_cleaner.query('country.str.contains("Denmark")')
se = gdp_cleaner.query('country.str.contains("Sweden")')
au = gdp_cleaner.query('country.str.contains("Australia")')


# <font color=#303F9F>Deciding to use a line chart to plot our data we can measure our data points for each year over the time span the data was collected. This is a great way to observe the data changes over time.</font>

# In[32]:


#Plotting Top 5 Countries Above the Mean GDP/Capita 2017
def high_gdp_line_chart():
    
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
    plt.ylabel('GDP')
    plt.title('Top 5 Global GDP Per Capita Above Mean')
    return plt.show()

high_gdp_line_chart()


# ## Question 1:
# 
# <font color=#303F9F>What countries rank highest in GDP above the global average for 2017?</font> <a id='eda'></a>

# <font color=#303F9F>We can also represent this as a pie chart to visualize our sample groups rank for GDP in 2017 (Top 5)</font>

# In[33]:


#Plotting a pie chart for top 5 countries above the mean GDP/Capita 2017
def high_gdp_pie():

    lux_pie = highest_gdp_avg_2017.iloc[0,2]
    no_pie = highest_gdp_avg_2017.iloc[1,2]
    dk_pie = highest_gdp_avg_2017.iloc[2,2]
    se_pie = highest_gdp_avg_2017.iloc[3,2]
    au_pie = highest_gdp_avg_2017.iloc[4,2]
    
    percent = lux_pie+no_pie+dk_pie+se_pie+au_pie

    pp1 = lux_pie/percent*100
    pp2 = no_pie/percent*100
    pp3 = dk_pie/percent*100
    pp4 = se_pie/percent*100
    pp5 = au_pie/percent*100

    labels = [r'Luxembourg (28.9 %)', r'Norway (24.4 %)',r'Denmark (16.5 %)', r'Sweden(15.2 %)',r'Australia (15.0)']
    sizes = [pp1,pp2,pp3,pp4,pp5]
    colors = ['g', 'b', 'r', 'y', 'c']
    explode = (0.3,0,0,0,0)  # only "explode" the 1st slice (i.e. 'Okay')

    plt.pie(sizes, explode=explode, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)
    # Set aspect ratio to be equal so that pie is drawn as a circle & Title.
    plt.title("Countries With Highest GDP/Captia Above Mean For 2017")
    plt.legend(labels, loc="upper right")
    plt.axis('equal')
    return plt.show()

high_gdp_pie()


# ## Observation Question 1: 
# 
# <font color=#303F9F>Luxembourg ranks 1st followed by Norway, Denmark, Sweden and Australia.</font>

# <a id='q2'></a>
# ## Question 2:
# <font color=#303F9F>From the top 5 GDP/Capita countries in 2017, on average which countries stay in school longer? Comparing  Men and Women between the ages of 15-24 </font> <a id='eda'></a>

# <font color=#303F9F>Deciding to use a line chart to plot our data we can measure our data points for each year over the time span the data was collected. This is a great way to observe the data changes over time.</font>

# In[34]:


#Calling functions we have created to address Our question
men_school.top_gdp_mschool()
women_school.top_gdp_wschool()


# ## Observation Question 2: 
# 
# <font color=#303F9F>It looks as though each country is experiencing a steady growth in education. However, Australian men and women are staying in school longer, yet they rank last of the top 5 (GDP above the global average for 2017). There are a few outliers in this observation however the strongest is Luxembourg. It would appear that the length of time men and women spend in school has nothing to do with the strength of its GDP, compared to the other samples.</font>

# <a id='q3'></a>
# ## Question 3:
# <font color=#303F9F>Are these Countries predominantly a service or industrial based economy?</font> <a id='eda'></a>

# <font color=#303F9F>Deciding to use a line chart to plot our data we can measure our data points for each year over the time span the data was collected. This is a great way to observe the data changes over time.</font>

# In[35]:


#Calling functions we have created to address our question
services_gdp.gdp_services_line_chart()
industry_gdp.gdp_industry_line_chart()


# ## Observation 3:
# 
# <font color=#303F9F>All five countries are majority service based economies. The true outlier is Norway, which remains mostly a services based economy. However it has the strongest industrial based sector of our 5 samples. Norway appears to have a fairly balanced industrial and service sector.</font>

# <a id='q4'></a>
# ## Question 4:
# <font color=#303F9F>For service and industry is there an increase or decrease in these secotors?</font>
# ## Observation 4:
# 
# <font color=#303F9F>There is an increase for the services sector of the economy for each of the five sample. All five samples excluding Norway are decreasing in their industrial based sectors.</font>

# <a id='q5'></a>
# ## Question 5:
# 
# <font color=#303F9F>Is Norway a balanced economy between its services and industrial sectors?</font>
# 

# In[36]:


#Calling functions (box plots) we have created to address our question
industry_gdp.gdp_percent_industry_norway_box();
services_gdp.gdp_percent_services_norway_box();


# ## Observation 5:
# 
# <font color=#303F9F>According to the box plots for percentage of GDP in each sector. We can see that the industrial sector is skewed heavily between 31-40% meaning that within the time period of 1970-2017 they must have had a few periods of boom and bust cycles. This is normal for the industrial sector or any economy. However if we look to the services box plot we will notice it remains relatively balanced compared to industrial.</font>  
# 
# 

# <a id='conclusions'></a>
# ## Conclusion
# 
# <font color=#303F9F>After observing the data and charting our finding we notice it leads to more questions. We have answered some of the basics however there is more to explore. The overall findings suggest that Norway is relatively balanced in education and economy in both services and industry sectors. We could gather more societal data and see how it compares with our other 5 samples. We could use it to develop more indicators. Through the insight that we have gathered we can look to find better ways to improve the economy and society overall. I believe this to be the greatest lesson of this exercise.</font>
# 
