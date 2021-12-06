rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
## Setup
import random

## Get the inputs
user_choice = int(input("Let's play Rock, Paper, Scissors! \nType either 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
game_images = [rock, paper, scissors]

if user_choice >=3 or user_choice < 0:
  print("You typed a bad number. You lose!")
else:
  print(f"Player selects: {game_images[user_choice]}")
  computer_choice = random.randint(0,2)
  print(f"Computer selects: {game_images[computer_choice]}")

  ## Compare the inputs
  if user_choice == computer_choice:
    print("It's a tie")
  # Rock wins against scissors.
  elif user_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and user_choice == 2:
    print("You lose.")
  # Scissors win against paper.
  elif user_choice == 2 and computer_choice == 1:
    print("You win!")
  elif computer_choice == 2 and user_choice == 1:
    print("You lose.")
  # Paper wins against rock.
  elif user_choice == 1 and computer_choice == 0:
    print("You win!")
  elif computer_choice == 1 and user_choice == 0:
    print("You lose.")
