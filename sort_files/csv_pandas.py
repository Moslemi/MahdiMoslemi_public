from pandas import DataFrame, read_csv
import n as int 
# General syntax to import a library but no functions:
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

# Enable inline plotting
Location = "/Users/MahdiMoslemi/Desktop/PycharmProjects/Triangular/CollectNodes"
df = pd.read_csv(Location, names=['X','Y','Z','W'], delimiter = ' ')

max_value= (df['Y'].max())
Sorted = df.sort_values(['X'], ascending=False)
Sorted.head(0)
print(Sorted)
min_value = (df['X'].min())

alpha = (df['W'].min())

print(alpha)
delta = 0.05

def function_():
    for lines in file:
        if min_value<= x <= max_value:
            for min_value + ((n-1)*delta) < x < min_value + (n*delta):
                num = df['Y'].max()
