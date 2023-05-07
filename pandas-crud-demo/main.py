from csv_crud import CsvCrud
from cfg import *

# Pandas Crud Demo
db = CsvCrud(csv_path("spain"))

# Get Result where dict
result = db.read({"state":"Alava"})
print(f"Read Where: \n {result} \n")

# Create new Row
    ## As dict
db.create({"state": "Sevilla","x": -30,"y":-400})

# Create new Row
    ## As list
db.create(["Cáceres",340,200])

# Update Row where id 1
db.update(1,{"state": ["Álava"],"x": [-30],"y":[-400]})

# Update Row where id 1
db.delete(4)

# Save Db 
db.save()

results = db.read()
print(f"Read All: \n {results} \n")



 