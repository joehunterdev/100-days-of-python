import turtle
from csv_crud import CsvCrud
from cfg import *

db = CsvCrud(csv_path("spain"))
image = image_path("spain")
screen = turtle.Screen()
screen.title(f"Provincias:" )
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor2(x, y):
#     print(f"{x} , {y} ")

def get_mouse_click_coor(x, y):
    
    for title in t:

        if title.distance(x,y) < 50: 
           print(f"{title.distance(x,y)}")
           print(f"Edit: {title}")
           msg = "Borrar Provincia"
           db.delete(db.get_id(title))
         # answer = st.screen.textinput("España Provincias","Borrar Provincia")
        else:
           msg = "Añadir Provincia"

    answer = st.screen.textinput("España Provincias",msg)

    st.goto(x,y)
    st.write(answer)
    db.create([answer,x,y])  
      
    db.save()





def save_exit():
    turtle.clearscreen()

# val = db.read()
# print(f"{val}")

print(f"Type db.df: {type(db.df)}")

# db.df.to_dict()


t = [turtle.Turtle()]
all_states = db.df.state

for idx,row in db.df.iterrows():

    current = db.read({"state":row}).to_dict()

    st = turtle.Turtle()
    st.penup()
    st.goto(row.x,row.y)
    st.write(row.state)
    st.hideturtle()
    t.append(st)

# for title in t:
#      title.showturtle()


screen.onscreenclick(get_mouse_click_coor)
# screen.onscreenclick(get_mouse_click_coor2,1)

screen.onkeypress(save_exit,"space")

screen.listen()

turtle.mainloop()