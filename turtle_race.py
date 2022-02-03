from turtle import Turtle,Screen
import random 

screen = Screen()
screen.setup(width=500,height=400)
user_input = screen.textinput("turtle race", "choose your turtle color that you wish to bet on: ")
colors = ['red','orange','yellow','green','blue']
y_cor = [-180,-80,0,80,180]
all_turtles = []
for i in range(5):
    t = Turtle('turtle')
    t.penup()
    t.color(colors[i])
    t.setpos(-230,y_cor[i])    
    all_turtles.append(t)

game_on = True
while game_on:
    for i in all_turtles:
        if i.xcor()>230:
            if i.pencolor() == user_input:
                print("You win")
            else:
                print("You lose")
            game_on = False
        else:
            i.forward(random.randint(0,10))
screen.exitonclick()
