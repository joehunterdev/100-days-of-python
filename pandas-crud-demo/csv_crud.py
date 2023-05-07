import pandas
from cfg import *

print(image_path("spain"))

print(csv_path("spain"))

## Read 

## All
csv = pandas.read_csv(csv_path("spain"))
print(f"Type: {type(print(csv))}" )
df = pandas.DataFrame(data = csv)

## Row
csv = pandas.read_csv(csv_path("spain"))
print(f"Type: {type(print(csv))}" )
df = pandas.DataFrame(data = csv)

print(f"DataFrame: {df}" )


## Create row as list
new_row_list = ["Malaga",-10,-200]
df.loc[len(df)]= new_row_list

## Create row as dataframe
new_row_obj = pandas.DataFrame({
  "state": ["Sevilla"],
  "x": [-30],
  "y":[-400]
}) 
df = pandas.concat([new_row_obj,df.loc[:]]).reset_index(drop=True)


## Update row id dataframe
new_row_obj = pandas.DataFrame({
  "state": ["Sevilla"],
  "x": [-30],
  "y":[-400]
}) 
df = pandas.concat([new_row_obj,df.loc[:]]).reset_index(drop=True)

## Update Row
  # find row
  # apply by id

# new_row_obj = pandas.DataFrame({
#   "state": ["Málaga"],
#   "x": [-30],
#   "y":[-400]
# }) 

# df = pandas.concat([new_row_obj,df.loc[:]]).reset_index(drop=True)

##,ignore_index = True
print(f"Updated: {df}" )
test_csv_path = csv_path("spain").replace("coords", "coords-2")
df.to_csv(test_csv_path, mode='w', index=False, header=False)    ###,ignore_index = True
# Append
df.to_csv(test_csv_path, mode='a', index=False, header=False)    


##Likely you will not need to store the index=False
# df.to_csv(csv_path("spain"), encoding='utf-8', index=False)
