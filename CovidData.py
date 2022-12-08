def total_deaths (deaths):
    tot = 0
    for i in deaths:
        tot += i
    return tot
    
def death_condition (data):
    for i in data:
        if i > 15000:
            print(i)
    
        
# import libraries for the project

import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt

# set the file path
path_to_file = '/Users/gihansenanayake/Documents/GIHAN/GIHAN/Fall 2022/CSC 140:141/Assignment/Project/'
# file name
file_name = 'COVID19_state.csv'

# load data to the dataframe
df_covid = pd.read_csv(path_to_file + file_name)

### save data to a new file 
path_to_file = '/Users/gihansenanayake/Documents/GIHAN/GIHAN/Fall 2022/CSC 140:141/Assignment/Project/'
new_file = 'New_Covid_data.csv'

### save data as CSV file
df_covid.to_csv(path_to_file + new_file, index=False)


# Output
print(df_covid.head(5))
print()
print()
print()

### Get the shape of the dataset
print(df_covid.shape)
print()
print()
print()

# ### Describe the dataset
print(df_covid.describe())
print()
print()
print()

### get info
print(df_covid.info())
print()
print()
print()

print(df_covid[['State', 'Infected','Deaths']])
print()
print()
print()


### slicing the data
print (df_covid[10:20])
print()
print()
print()

death_col = df_covid['Deaths']
print(death_col)
print()
print()

print("Total Deaths in USA: ", total_deaths(death_col))
print()
print()
print()

### Get the State with most Deaths and least deaths
print(df_covid.loc[df_covid['Deaths'].idxmax()])
print()
print()
print(df_covid.loc[df_covid['Deaths'].idxmin()])
print()
print()

### States no.of Deaths Greater than 15000
print(death_condition(death_col))
print()
print()

# Get the State with most Hospitals
print(df_covid.loc[df_covid['Hospitals'].idxmax()])
print()
print()
print(df_covid.loc[df_covid['Hospitals'].idxmin()])
print()
print()

### Extending the Dataframe
df_covid["Country"] = "USA"
print(df_covid)
print()
print()
print()


### condition to find which state has 3 airports and 8.5 pollution rate


print(df_covid[
    (
        (df_covid['Med-Large Airports'] == 3) 
        &
        
        (df_covid['Pollution']== 8.5)
    )
    
]   )
      
      
#### sort the data by deaths and 

print(df_covid.sort_values(by=['Deaths', 'Infected'], ascending = True))


# plot of the Death people
death_number = df_covid['Deaths'].head(5)
states = df_covid['State'].head(5)
plt.xlabel('States')
plt.ylabel('No.Of Deaths')
plt.title('Number Of Deaths by States')
plt.bar(states, death_number)
plt.show()


# Plot of Income and GDP
df_covid[['Income', 'GDP']].plot()
plt.xlabel('States')
plt.ylabel('Values')
plt.title('Income and GDP')
plt.show()



