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

# Output
print(df_covid.head())
print()
print()
print()

### Get the shape of the dataset
print(df_covid.shape)
print()
print()
print()

### Describe the dataset
print(df_covid.describe)
