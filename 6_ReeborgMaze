Goal: Find the maze exit
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
reeborg.ca

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
# Call functions    
loop_check = 0 
while not at_goal():
    if loop_check < 4:
        if right_is_clear():
            turn_right()
            move()
            loop_check += 1
        elif front_is_clear():
            move()
            loop_check = 0
        else:
            turn_left()
            loop_check += 1  
#turning right if it can, going straight ahead if it can’t turn right, 
#or turning left as a last resort.        

#front_is_clear() or wall_in_front(), at_goal()   
#24 lines code = goal
#front_is_clear() right_is_clear()
#wall_in_front() wall_on_right()
