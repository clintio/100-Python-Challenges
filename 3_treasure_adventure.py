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
print("Welcome to Treasure Island.")
print("Find Captain Flint's treasure by typing your choices.") 

choice1 = input('\nStart walking either "left" or "right"? ').lower()
if choice1 == "left": #Good choice
  choice2 = input('\nYou get to a lake and see a little island in the middle. \nHow do you get there? Either "wait" or "swim"? ').lower()
  
  if choice2 == "wait": #Good choice
    choice3 = input('\nYou find a boat and sail to the island. You enter a large house with 3 colored doors.\nWhich door do you open? Either "red","yellow", or "blue"? ').lower()
    
    if choice3 == "yellow": #Winner
      print("\nYou found the treasure! You Win!")
    
    # For the gameovers
    elif choice3 == "red":
      print("\nThe floor lights on fire and burns you alive. Game Over.")
    elif choice3 == "blue":
      print("\nBeasts jump out and devour you. Game Over")
    else:
      print("\nYou chose a door that doesn't exist. That means you don't exist. Game Over.")

  elif choice2 == "swim":
    print("\nYou're eaten by pirahanas. Game Over.")
  else:
    print('\nSorry, we didn\'t recognize your answer resulting in Game Over.\nFor next time, type one of the "choices" provided.')

elif choice1 == "right":
  print("\nYou fall into a hole and die. Game over")
else:
  print('\nSorry, we didn\'t recognize your answer resulting in Game Over.\nFor next time, type one of the "choices" provided.')
