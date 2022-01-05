##Hangman game
#Setup
import random
from hangman_words import word_list
from replit import clear

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

#Intro
from hangman_art import logo
print(logo)

#Debug code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
old_guesses = []
display = []
for _ in range(word_length):
    display += "_"

#Main function
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in old_guesses: 
      print(f'You\'ve already guessed the letter "{guess}".')
    else:
      clear()
      #Check the letter
      for position in range(word_length):
          letter = chosen_word[position]
          # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
          if letter == guess:
              display[position] = letter

      #If wrong
      if guess not in chosen_word:
          print(f'The letter "{guess}" is not in the word.')
          lives -= 1
          if lives == 0:
              end_of_game = True
              print("You lose.")

      #Join the blanks and letters
      print(f"{' '.join(display)}")

      #Winner?
      if "_" not in display:
          end_of_game = True
          print("You win.")

      from hangman_art import stages
      print(stages[lives])
    old_guesses += guess
