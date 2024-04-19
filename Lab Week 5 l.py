# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 16:30:16 2024

@author: ChelseySSS
"""

#SHIHAN ZHAO

import pandas as pd

#1. It's a puzzle! Load these three dataframes and explore their structure.
#Then combine them so that the result is a single dataframe with the columns 
#"date", "place", "value1", "value2", with the date columns being datetime 
#objects that run from 1/2020 to 10/2021, without modifying any starter code.

data1 = {'date':['2020-1-1', '2020-4-1', '2020-7-1', '2020-10-1'],
         'place1':[39, 17, 20, 88],
         'place2':[55, 88, 19, 42]}

data2 = {'date':['2020-01-01', '2020-04-01', '2020-07-01', '2020-10-01',
                 '2021-01-01', '2021-04-01', '2021-07-01', '2021-10-01'],
         'place1':[1, 4, 7, 2, 5, 8, 11, 13],
         'place2':[2, 5, 8, 6, 6, 9, 13, 15]}

data3 = {'date':['2021-1-1', '2021-4-1', '2021-7-1', '2021-10-1']*2,
         'place':['place1']*4 + ['place2']*4,
         'value1':[33, 43, 53, 34, 35, 46, 47, 48]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
df3 = pd.DataFrame(data3)


# Display the first few rows of each dataframe 
print("DataFrame 1:")
print(df1.head())

print("\nDataFrame 2:")
print(df2.head())

print("\nDataFrame 3:")
print(df3.head())



# Convert date columns to datetime
df1['date'] = pd.to_datetime(df1['date'])
df2['date'] = pd.to_datetime(df2['date'])
df3['date'] = pd.to_datetime(df3['date'])

# Melt df1 and df2 to match df3's format
df1_melted = df1.melt(id_vars=['date'], var_name='place', value_name='value1')
df1_melted['place'] = df1_melted['place'].str.replace('place', 'place')

df2_melted = df2.melt(id_vars=['date'], var_name='place', value_name='value2')
df2_melted['place'] = df2_melted['place'].str.replace('place', 'place')

# Combine the DataFrames
# First merge df1_melted with df2_melted on 'date' and 'place'
df_combined = pd.merge(df1_melted, df2_melted, on=['date', 'place'], how='outer')

# Then merge the result with df3 on 'date' and 'place'
final_df = pd.merge(df_combined, df3, on=['date', 'place'], how='outer', suffixes=('_old', ''))

# Now selecting and renaming columns as necessary, 'value1' from df3 takes priority
final_df['value1'] = final_df['value1'].fillna(final_df['value1_old'])
final_df = final_df.drop(columns=['value1_old'])

print(final_df)



#2. You had to do some merging in part 1. If you did not already, go back and use
#some assert statements to verify that the dataframes did what you expected.


# Convert date columns to datetime
df1['date'] = pd.to_datetime(df1['date'])
df2['date'] = pd.to_datetime(df2['date'])
df3['date'] = pd.to_datetime(df3['date'])

# Assertions to verify date conversion
assert df1['date'].dtype == 'datetime64[ns]', "df1 date column is not datetime type"
assert df2['date'].dtype == 'datetime64[ns]', "df2 date column is not datetime type"
assert df3['date'].dtype == 'datetime64[ns]', "df3 date column is not datetime type"

# Melt df1 and df2 to match df3's format
df1_melted = df1.melt(id_vars=['date'], var_name='place', value_name='value1')
df1_melted['place'] = df1_melted['place'].str.replace('place', 'place')

df2_melted = df2.melt(id_vars=['date'], var_name='place', value_name='value2')
df2_melted['place'] = df2_melted['place'].str.replace('place', 'place')

# Assertions to verify melting process
assert 'value1' in df1_melted.columns, "value1 column missing in df1_melted"
assert 'value2' in df2_melted.columns, "value2 column missing in df2_melted"

# Combine the DataFrames
df_combined = pd.merge(df1_melted, df2_melted, on=['date', 'place'], how='outer')
final_df = pd.merge(df_combined, df3, on=['date', 'place'], how='outer', suffixes=('_old', ''))

# Assertions to check combined DataFrame
assert not final_df['date'].isnull().any(), "Null values in date column in final_df"
assert not final_df['place'].isnull().any(), "Null values in place column in final_df"
assert 'value1' in final_df.columns and 'value2' in final_df.columns, "Missing value columns in final_df"
assert len(final_df) == (len(df1_melted) + len(df2_melted) + len(df3)) / 2, "Final DataFrame length mismatch"

# Column selection and renaming
final_df['value1'] = final_df['value1'].fillna(final_df['value1_old'])
final_df = final_df.drop(columns=['value1_old'])

print(final_df)



#3. Is the dataframe from part 1 in long or wide format? Write code to convert it
#into the other.

# The DataFrame from part 1 is in long format 

# Pivot the table to wide format
wide_format_df = final_df.pivot(index='date', columns='place')

# Reset the index to make 'date' a column again and flatten the MultiIndex in columns
wide_format_df.reset_index(inplace=True)
wide_format_df.columns = ['_'.join(col).strip() if col[1] else col[0] for col in wide_format_df.columns.values]

print(wide_format_df)





