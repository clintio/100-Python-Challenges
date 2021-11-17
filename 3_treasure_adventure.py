print("Welcome to Treasure Island.")
print("Find Captain Flint's treasure by typing your choices.") 

#Write your code below this line 👇
## Question 1
user_start = input('\nStart walking either "left" or "right"? ').lower()
if user_start == "right":
  print("\nYou fall into a hole and die. Game over")

## Question 2
elif user_start == "left":
  user_lake = input('\nYou get to a lake and see a little island in the middle. \nHow do you get there? Either "wait" or "swim"? ').lower()
  if user_lake == "swim":
    print("\nYou're eaten by pirahanas. Game Over.")
  
  ## Question 3
  elif user_lake == "wait":
    user_door = input('\nYou find a boat and sail to the island. \nYou enter a large house with 3 colored doors.\nWhich door do you open? Either "red","yellow", or "blue"? ').lower()

    # For the gameovers(x2)
    if user_door == "red":
      print("\nThe floor lights on fire and burns you alive. Game Over.")
    elif user_door == "blue":
      print("\nBeasts jump out and devour you. Game Over")
    # For the winner
    elif user_door == "yellow":
      print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
      print("The lights go out. A neon sign appears: \nYou found the treasure! You Win!")
    else:
      print("\nYou chose a door that doesn't exist. That means you don't exist. Game Over.")

  # Catchall
  else:
    print('\nSorry, we didn\'t recognize your answer resulting in Game Over.\nFor next time, type one of the "choices" provided.')
else:
  print('\nSorry, we didn\'t recognize your answer resulting in Game Over.\nFor next time, type one of the "choices" provided.')
