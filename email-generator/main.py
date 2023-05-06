
from cfg import *
import csv

# Get Template
# Map Placeholders
def generate_template(template_name,mapping):
    file = str(open(TEMPLATES_FOLDER+template_name, "r").read())
    for placeholder,value in mapping:
        file = file.replace(placeholder,value)
    return file

def export_template(file_name,content):
    with open(OUTBOX_FOLDER+file_name, mode ="w") as file:
        file.write(content)
        
# def load_contacts(file_name):
#     with open(CONTACTS_FOLDER+file_name, newline='\n') as csvfile:
#           db =  csv.reader(csvfile, delimiter=',', quotechar='|')
#           return db

# print(load_contacts("invited.csv"))

with open(CONTACTS_FOLDER+"invited.csv", newline='\n') as csvfile:
     db =  csv.reader(csvfile, delimiter=',', quotechar='|')
     for data in db:
        print(data[0])
        mapping = [('[first_name]', data[0]),('[email]',data[1]),('[job]', data[2])]
        export_template(data[0]+".html",generate_template("basic.html",mapping))

## Better to use pandas





