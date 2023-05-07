import pandas
from cfg import *

## Paths
print(image_path("spain"))
print(csv_path("spain"))

# Read 

## All
csv = pandas.read_csv(csv_path("spain"))
print(f"Type: {type(print(csv))}" )
df = pandas.DataFrame(data = csv)

## Single Row
result = df.iloc[[0]]
print(f"Result: {result}" )

## Where
results_where = df[df.state.isin(["Alava"])]
print(f"Result Where: {result}" )

## Get Id where row
row = results_where
index = row.index.tolist()

print(f"Index from row: {index}")

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

#Updated
updated_row_obj = pandas.DataFrame({
  "state": ["Álava"],
  "x": [-30],
  "y":[-400]
})

df.iloc[[index]]  = updated_row_obj

#Delete
df.drop([3], axis=0, inplace=True)
#df.drop([index], axis=0, inplace=True)


# df = pandas.concat([new_row_obj,df.loc[:]]).reset_index(drop=True)

##,ignore_index = True
print(f"Updated: {df}" )
test_csv_path = csv_path("spain").replace("coords", "coords-2")
df.to_csv(test_csv_path, mode='w', index=False, header=False)    ###,ignore_index = True
# Append
# df.to_csv(test_csv_path, mode='a', index=False, header=False)    


##Likely you will not need to store the index=False
# df.to_csv(csv_path("spain"), encoding='utf-8', index=False)

class CsvCrud():
   
  def __init__(self,fpath):
    
    self.row_id = 0
    self.df = self.load(fpath)

    pass
  
  def create_row():
    pass
  
  def read():
    pass
 
  def read_row():
    pass
   
  def update():
    pass
 
  def delete():
    pass
  
  def load(self,fpath):

      return  pandas.DataFrame(data = pandas.read_csv(fpath))
 
db = CsvCrud(csv_path("spain"))


print(f"Db Object: {db.df}")
