# importing libraries
import pandas as pd # import pandas
import re # import regular expression

# create reusable path
mypath = "C:\\Users\\ACER\\OneDrive\\Desktop\\python_test\\"

#### LOADING THE DATA ####
df = pd.read_csv(f'{mypath}datasets\\pokemon_data.csv')
# df = pd.read_excel(f'{mypath}datasets\\pokemon_data.xlsx')
# df = pd.read_csv(f'{mypath}datasets\\pokemon_data.txt',delimiter='\t')

# print(df.head(10))
# print(df.tail())

#### READING THE DATA ####

## read headers
# df.columns

## read each column/s
# df['Name'] # show a specific column
# print(df['Name'][0:2]) # specify the number of records to be shown [start_index:num_items_to_display]
# df[['Name','Type 1', 'Type 2']] # show specific multiple columns

## read each row/s

### using .iloc
# f=df.iloc[10] # get each row by index

# print(df.iloc[4:9,9:11]) # multiple rows by slice object [start_slice:stop_slice]

### iterating through rows using for loop & .iterrows()
# for index, row in df.iterrows():
#     print(index, row)

# for index, row in df.iterrows():
#     print(index, row["Name"])

### using .loc
# print(df.loc[df['Type 1'] == 'Bug' ])

# d = df.loc[(df['Type 1'] == 'Bug') | (df['Type 2'] == 'Flying')]

## read a specific location (row, col)
# print(df.iloc[2,2])

#### SHOW DATASET SCHEMA/INFO ####
# print(df.dtypes) # shows datatypes of each column
# print(df.info()) # prints info about a DataFrame including the index dtype and columns, non-null values and memory usage
# print(df.shape) # displays total number of rows and columns of dataframe (#row,#col)
# print(df.describe()) # shows summary of stats using various statistical methods for each column

#### FILTERING DATA ####

## by multiple conditions
# d=df.loc[(df['Type 1'] == 'Grass') | (df['Type 1'] == 'Fire')][['Type 1', 'Name','Attack']]

## by specific string
# # d=df.loc[~df['Name'].str.contains('Mega')]
# d=df.loc[df['Name'].str.contains('^Pi[A-Z]*', flags=re.IGNORECASE, regex=True)]
# print(d)
# df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)]

#### CONDITIONAL CHANGES ####
# df.loc[df['Type 1'] == 'Flamer', 'Type 1'] = 'Fire'
# df.loc[df['Type 1'] == 'Fire', 'Legendary'] = 'True'
# # print(df.loc[df['Type 1'] == 'Fire', ['Type 1','Legendary']])
# df.loc[df['Type 1'] == 'Fire', ['Generation','Legendary']] = 'test 1'

#### ADDING COLUMN ####
# df['Total'] = df['HP'] + df['Attack'] + df['Defense']

#### DELETING COLUMN ####
# new_df = df.drop(columns=['Total'])

#### SAVING DATA ####
# d.to_csv('modified_pokemon.csv')

#### AGGREGATING DATA ####
# gb=df.groupby(['Type 1']).mean(numeric_only=True)
# print(gb)
# gb=df.groupby(['Type 1']).sum(numeric_only=True)
# print(gb)
# gb=df.groupby(['Type 1']).count()
# print(gb)


