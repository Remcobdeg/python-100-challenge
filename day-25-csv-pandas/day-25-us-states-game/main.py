import turtle
import pandas as pd

from turtle_text import TextTurtle

screen = turtle.Screen()
screen.title("US states game")

pen = TextTurtle()

#process for adding an image to turtle
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#read the states data
states_data = pd.read_csv("50_states.csv")

count = 0
total = len(states_data.state.array)

while count < total:
    guessed_state = turtle.textinput(title=f"{count}/{total} states correct",prompt="What's another US state?").title()
    if guessed_state == "Exit":
        break
    elif guessed_state in states_data.state.array:
        state,x,y = (states_data.loc[states_data.state == guessed_state].values[0]) #.item()[0] would also work
        pen.writeText(state,x,y)
        count += 1
        #remove the row to prevent it from being counted
        states_data.drop(states_data.index[states_data.state == guessed_state])

states_data.state.to_csv("states_to_learn.csv")

screen.exitonclick()




# #process to get coordinates from click
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop() #alternative to exit on click -- necessary here because our function works with a click
#
