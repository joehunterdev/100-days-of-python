import turtle
import pandas
from cfg import *

screen = turtle.Screen()
screen.title(f"Provincias:" )
image = PATH+"\game\\spain\\"+"map.gif"
screen.addshape(image)
turtle.shape(image)
columns = ["state","x","y"]
# data = pandas.read_csv(PATH+"\game\spain\\"+"states.csv")

# all_states = data.state.to_list()
# df = pandas.DataFrame(data=data)
# print(df)
new_set = pandas.DataFrame(data=columns)
new_set.to_dict()

def get_mouse_click_coor(x, y):
    t.goto(x,y)
    answer = t.screen.textinput("España Provincias","Añadir Provincia")
    t.write(answer)
    new_set.append({'state': answer, 'x': x, 'y':y})

def save_exit():
    turtle.clearscreen()
    
t = turtle.Turtle()

# while IN_GAME:
    
    
# data of Player and their performance
# data = {
#     'state': "[data.state]",
#     'x': 0,
#     'y': 0,
# }
 
# Make data frame of above data

    
# new_set.to_list()
    # t.screen.onclick()
screen.onscreenclick(get_mouse_click_coor)    
screen.onkeypress(save_exit,"space")
print(f"{new_set}")

new_set.to_csv(PATH+"\game\spain\\"+"states2.csv", mode='a', index=False, header=False)    

# df = pandas.DataFrame(new_set)
 
# append data frame to CSV file
# df.to_csv(PATH+"\game\spain\\"+"states_3.csv", mode='a', index=False, header=False)
 
# print message
print("Data appended successfully.")    

screen.listen()
turtle.mainloop()