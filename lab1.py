"""Lab 1"""
import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library

df_can = pd.read_excel(
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx",
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)
print('Data downloaded and read into a dataframe!')

# Let's view the top 5 rows of the dataset
print(df_can.head())

# We can also view the bottom 5 rows of the dataset
print(df_can.tail())

# This method can be used to get a short summary of the dataframe.
print(df_can.info(verbose=False))

# To get the list of column headers
print(df_can.columns)

# to get the list of indices
print(df_can.index)

# To get the index and columns as lists
df_can.columns.tolist()
df_can.index.tolist()

# To view the dimensions of the dataframe
print(df_can.shape) # size of dataframe (rows, columns)

# Let's clean the data set to remove a few unnecessary columns
# in pandas axis=0 represents rows (default) and axis=1 represents columns.
df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
print(df_can.head(2))

# Let's rename the columns so that they make sense
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
print(df_can.columns)

# We will also add a 'Total' column that sums up the total immigrants by country over the entire period 1980 - 2013
# df_can['Total'] = df_can.sum(axis=1)

# We can check to see how many null objects we have in the dataset as follows:
print(df_can.isnull().sum())

# let's view a quick summary of each column in our dataframe
print(df_can.describe())

# Let's try filtering on the list of countries
print(df_can.Country)  # returns a series

# Let's try filtering on the list of countries ('Country') and the data for years: 1980 - 1985.
print(df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]]) # returns a dataframe
# notice that 'Country' is string, and the years are integers. 
# for the sake of consistency, we will convert all column names to string later on.

# to do a query by a specific country
df_can.set_index('Country', inplace=True)
# tip: The opposite of set is reset. So to reset the index, we can use df_can.reset_index()

print(df_can.head(3))

# optional: to remove the name of the index
df_can.index.name = None

# Let's view the number of immigrants from Japan (row 87) for the following scenarios: 
# 1. The full row data (all columns) 2. For year 2013 3. For years 1980 to 1985

# 1. the full row data (all columns)
print(df_can.loc['Japan'])

# alternate methods
# df_can.iloc[87]
# df_can[df_can.index == 'Japan']

# 2. for year 2013
print(df_can.loc['Japan', 2013])

# alternate method
# year 2013 is the last column, with a positional index of 36
# df_can.iloc[87, 36]

# 3. for years 1980 to 1985
print(df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]])

# Alternative Method
# df_can.iloc[87, [3, 4, 5, 6, 7, 8]]

# Column names that are integers (such as the years) might introduce some confusion
# To avoid this ambuigity, let's convert the column names into strings: '1980' to '2013'.
df_can.columns = list(map(str, df_can.columns))
[print (type(x)) for x in df_can.columns.values] #<-- uncomment to check type of column headers

# Since we converted the years to string, let's declare a variable that will allow us to easily call upon the full range of years:
# useful for plotting later on
years = list(map(str, range(1980, 2014)))
print(years)

# To filter the dataframe based on a condition, we simply pass the condition as a boolean vector.
# 1. create the condition boolean series
condition = df_can['Continent'] == 'Asia'
print(condition)

# 2. pass this condition into the dataFrame
df_can[condition]

# we can pass multiple criteria in the same line.
# let's filter for AreaNAme = Asia and RegName = Southern Asia

df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')]

# note: When using 'and' and 'or' operators, pandas requires we use '&' and '|' instead of 'and' and 'or'
# don't forget to enclose the two conditions in parentheses

# Before we proceed: let's review the changes we have made to our dataframe.
print('data dimensions:', df_can.shape)
print(df_can.columns)
print(df_can.head(2))

# Let's start by importing matplotlib and matplotlib.pyplot as follows:
import matplotlib as mpl
import matplotlib.pyplot as plt

print('Matplotlib version: ', mpl.__version__)  # >= 2.0.0

print(plt.style.available)
mpl.style.use(['ggplot']) # optional: for ggplot-like style

# Question: Plot a line graph of immigration from Haiti using df.plot().
# First, we will extract the data series for Haiti.
haiti = df_can.loc['Haiti', years] # passing in years 1980 - 2013 to exclude the 'total' column
print(haiti.head())

# Next, we will plot a line plot by appending .plot() to the haiti dataframe.
haiti.plot()

# Also, let's label the x and y axis using plt.title(), plt.ylabel(), and plt.xlabel() as follows:
haiti.index = haiti.index.map(int) # let's change the index values of Haiti to type integer for plotting
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.show() # need this line to show the updates made to the figure

# We can clearly notice how number of immigrants from Haiti spiked up from 2010 as Canada stepped up its efforts to accept refugees from Haiti. 
# Let's annotate this spike in the plot by using the plt.text() method.
haiti.plot(kind='line')

plt.title('Immigration from Haiti')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')

# annotate the 2010 Earthquake. 
# syntax: plt.text(x, y, label)
plt.text(2000, 6000, '2010 Earthquake') # see note below

plt.show() 

# Question: Let's compare the number of immigrants from India and China from 1980 to 2013.
# Step 1: Get the data set for China and India, and display the dataframe.
df_CI = df_can.loc[['India', 'China'], years]

# Step 2: Plot graph. We will explicitly specify line plot by passing in kind parameter to plot().
df_CI.plot(kind='line')

# Recall that pandas plots the indices on the x-axis and the columns as individual lines on the y-axis. 
# Since df_CI is a dataframe with the country as the index and years as the columns, 
# we must first transpose the dataframe using transpose() method to swap the row and columns.
df_CI = df_CI.transpose()
print(df_CI.head())

# Go ahead and plot the new transposed dataframe. Make sure to add a title to the plot and label the axes.
df_CI.index = df_CI.index.map(int) # let's change the index values of df_CI to type integer for plotting
df_CI.plot(kind='line')

plt.title('Immigration from China and India')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')
plt.show() 

# Question: Compare the trend of top 5 countries that contributed the most to immigration to Canada.
#Step 1: Get the dataset. Recall that we created a Total column that calculates cumulative immigration by country. 
#We will sort on this column to get our top 5 countries using pandas sort_values() method.
    
inplace = True # paramemter saves the changes to the original df_can dataframe
df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)

# get the top 5 entries
df_top5 = df_can.head(5)

# transpose the dataframe
df_top5 = df_top5[years].transpose() 

print(df_top5)


#Step 2: Plot the dataframe. To make the plot more readeable, we will change the size using the `figsize` parameter.
df_top5.index = df_top5.index.map(int) # let's change the index values of df_top5 to type integer for plotting
df_top5.plot(kind='line', figsize=(14, 8)) # pass a tuple (x, y) size



plt.title('Immigration Trend of Top 5 Countries')
plt.ylabel('Number of Immigrants')
plt.xlabel('Years')


plt.show()
