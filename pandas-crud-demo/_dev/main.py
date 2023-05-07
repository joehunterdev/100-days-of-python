import turtle
import pandas
from cfg import *

screen = turtle.Screen()
screen.title(f"Us Capitals:" )
image = PATH+"blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
columns = ["state","x","y"]
data = pandas.read_csv(PATH+"50_states.csv",header=None, 
     names=columns,skiprows=1)

data = pandas.read_csv(PATH+"50_states.csv")
all_states = data.state.to_list()
df = pandas.DataFrame(data=data)

 
score = 0
guesses = []
while len(guesses) <=4:
    
    answer = screen.textinput(title="Guess the state:" + str(score) + "/ 50",prompt="Whats another state name ?")
    answer.title()

    if answer in all_states:
        
        result = df[df.state == answer]
        guesses.append(result)
        # result.to_dict()
        print(f"State: {result.state}")
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # print(f"Item {result.x.item()}")
        t.goto(int(result.x.item()),int(result.y.item()))
        t.write(result.state.item(),False,"Center")
        score +=1
        
else: 
        t.screen.clear()
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(0,-600)
        missed_states = filter(lambda x: x not in guesses, all_states)
        print(f"{missed_states}")
        # result = [a for a in A if a not in subset_of_A]
        t.write("You Win !!!",False,"Center",font= ("Arial",10,"Black"))
        
               
    # else:
        
    # #    answer = screen.textinput(title="Guuess the state",prompt=" 2 Whats another state name ?")
    # continue
        

    
# state_found["x"]
# state_found["y"]

screen.listen()
turtle.mainloop()