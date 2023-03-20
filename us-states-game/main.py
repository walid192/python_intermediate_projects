from os import stat
import turtle
import pandas


screen=turtle.Screen()
screen.title("U.S_States_Game")
image="Us_states_game_with_turtle/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


score=0

data=pandas.read_csv("Us_states_game_with_turtle/us-states-game-start/50_states.csv")
states_names=data.state
states_list=pandas.Series.to_list(states_names)

    
Guessed_states=[]   


while score<50:
    answer=screen.textinput("Guess the state","what's a state name").title()
    if answer=="Exit":
         # creating a csv file containing all the non-guessed states
        non_guessed_states=[]
        for state in states_list:
            if  (state not in Guessed_states):
                 non_guessed_states.append(state)
                 new_csv_data=pandas.DataFrame(non_guessed_states)
                 new_csv_data.to_csv("states_to_learn.csv")
        break
    if answer in states_list:
        score+=1
        Guessed_states.append(answer)
        screen.title(f"U.S_States_Game       score : {score}/50")
        
        #write the state name
        row=data[data.state==answer]
        x=row.x
        y=row.y
        state_name=turtle.Turtle("circle")
        state_name.hideturtle()
        state_name.penup()
        state_name.goto(float(x),float(y))
        state_name.write(answer)
    
    
   
        

