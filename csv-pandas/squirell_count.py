import pandas
from cfg import *
data = pandas.read_csv(PATH+'2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')  

## Get all unique furr colors
unique_colors = data['Primary Fur Color'].drop_duplicates()
unique_colors.pop(0)
 
df2 = []
# count = 0
for color in unique_colors:
    df2.append({color:int(data['Primary Fur Color'].isin([color]).sum(0))}) 
    # df.append(d)
# all_colors  = all_colors_count["Gray"]


print(df2)

## Generate dataframe
# print(f"{df2}")
df3 = pandas.DataFrame(data=df2)
df3 = pandas.to_csv(PATH+'Squirrel_Color_Data.csv')  

print(df3)
 
 ## Using Dict

data_dict = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count":[df2[0],df2[1],df2[2]]
}

df4 = pandas.DataFrame(data=data_dict)
df4 = pandas.to_csv(PATH+'Squirrel_Color_Data.csv')  

print(df4)