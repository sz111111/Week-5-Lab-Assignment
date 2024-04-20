# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 16:34:18 2024

@author: ChelseySSS
"""



#SHIHAN ZHAO

import pandas as pd

url_to_csv = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv'

df = pd.read_csv(url_to_csv)

# 1) Create a groupby object using "clarity" and "color" as the keys

# Create a groupby object using "clarity" and "color" as the keys
grouped = df.groupby(['clarity', 'color'])



# 2) Display the describe() output JUST for group color=E, clarity=SI2

# Display the describe() output for diamonds with color='E' and clarity='SI2'
description = grouped.get_group(('SI2', 'E')).describe()
print(description)



# 3) Display the max value for price in each group

# Display the max value for price in each group
max_price = grouped['price'].max()
print(max_price)



# 4) Display the min value for price in each group

# Display the min value for price in each group
min_prices = grouped['price'].min()
print(min_prices)



# 5) Write four different functions:
#    - one that works with map on the values in a column
#    - one that works with apply on the values in a row
#    - one that works with apply on the values in a column
#    - one that works with apply on a groupby object

# Function that works with map on the values in a column
def double_values(x):
    return x * 2

# Apply the map function to the 'carat' column
df['double_carat'] = df['carat'].map(double_values)

# Function that works with apply on the values in a row
def price_per_carat(row):
    return row['price'] / row['carat']

# Apply the function to each row
df['price_per_carat'] = df.apply(price_per_carat, axis=1)

# Function that works with apply on the values in a column
def square_values(x):
    return x ** 2

# Apply the function to the 'depth' column
df['squared_depth'] = df['depth'].apply(square_values)

# Function that works with apply on a groupby object
def average_price(group):
    return group['price'].mean()

# Create a groupby object and apply the function
grouped = df.groupby(['clarity', 'color'])
average_prices = grouped.apply(average_price)

# Print results
print("Double Carat Example:\n", df[['carat', 'double_carat']].head())
print("Price Per Carat Example:\n", df[['price', 'carat', 'price_per_carat']].head())
print("Squared Depth Example:\n", df[['depth', 'squared_depth']].head())
print("Average Prices by Clarity and Color:\n", average_prices.head())



# 6) Display only the maximum price for each clarity.

# Group by 'clarity' and calculate the maximum price for each clarity
max_price_per_clarity = df.groupby('clarity')['price'].max()

# Print the result
print(max_price_per_clarity)



# 7) Stretch goal! Which clarity of diamond has the diamond that is
#    the largest outlier in size (carats) from the mean for that group?

# Calculate the mean carat for each clarity group
mean_carats = df.groupby('clarity')['carat'].mean()

# Function to calculate the absolute deviation from the group mean
def deviation_from_mean(row):
    return abs(row['carat'] - mean_carats[row['clarity']])

# Apply the function to compute deviations
df['deviation_from_mean'] = df.apply(deviation_from_mean, axis=1)

# Find the row with the maximum deviation
max_deviation_row = df.loc[df['deviation_from_mean'].idxmax()]

# Display the clarity of the diamond with the largest outlier in size
print("Clarity with the largest carat size outlier:", max_deviation_row['clarity'])
print("Details of this diamond:", max_deviation_row)




