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


