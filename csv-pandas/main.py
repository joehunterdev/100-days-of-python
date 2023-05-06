import pandas 
import numpy
from cfg import *
data = pandas.read_csv(PATH+'weather_data.csv')  

# Get csv 
# print(data)

# # Get csv col
# print(data["day"])

# To dict
dict = data.to_dict()

# To List (easier to work with)
# list = data.Index.to_list()

## Calculate avg temp
avg  = data['temp'].mean()
print(f"Avg: {avg}")

## Retrieve max
max  = data['temp'].max()
print(f"Max: {max}")


# Get a row based on val
one_col = data[data.day == 'Wednesday']
one_col2 = data.loc[data['day'] == 'Monday']
print(f"One Col: {one_col2}")

## Get row based on argument
max_temp_row = data.loc[data['temp'] == max]
print(f"Max Temp: {max_temp_row}")

## Get mon temp in celsius as farenheight
def fahr_to_celsius(temp_fahr):
    temp_celsius = (temp_fahr - 32) * 5 / 9
    return temp_celsius

mondays =  data[data.day == 'Monday']
highest_c = fahr_to_celsius(int(mondays["temp"].max()))
print(f"Heighest Mon C: {highest_c}")

## Create a dataframe
d = {'col1': [1, 2], 'col2': [3, 4]}
df = pandas.DataFrame(data=d)
df.to_csv(PATH+"new_d.csv")
print(df)
 