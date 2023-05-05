
import os 

## Paths
PATH = os.path.dirname(os.path.realpath(__file__))
DATA_FOLDER = "\\data\\"
DATA_PATH =  PATH+DATA_FOLDER

# More path tricks
absolute_path = os.path.dirname(__file__)
relative_path = "src/lib"  # to go up dir ../somedatadir/file
full_path = os.path.join(absolute_path, relative_path)

## Open File
# file = open(DATA_PATH+"text.txt", "r")
# print(file.read())

## Open and close resource
with open(DATA_PATH+"text.txt", "r") as file:
    print(file.read())

# Change mode to w
    # if file doesnt exist it will create it for you
with open(DATA_PATH+"new_text.txt", mode ="w") as file:
    file.write("heres some new text ")
    
 # A mode will append
 with open(DATA_PATH+"new_text.txt", mode ="a") as file:
    file.write("heres some newer text ")

