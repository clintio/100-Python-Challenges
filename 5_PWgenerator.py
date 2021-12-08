
# Source: Dr. Angela
# https://www.udemy.com/course/100-days-of-code/learn/lecture/18085749?start=225#announcements

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# For debugging:
#nr_letters = 4
#nr_symbols = 2
#nr_numbers = 2
#
#print(f"{nr_letters} letters")
#print(f"{nr_symbols} symbols")
#print(f"{nr_numbers} numbers")


## Eazy Level - Order not randomized.
# Simply concatenating values as strings
# e.g. 4 letters, 2 symbols, 2 numbers = JduE&!91

#password ="" # Setup
#
#for letter in range(1,nr_letters+1):
#    random_letter = random.choice(letters)
#    password += random_letter 
#    # print(password) #Debug
#
#for symbol in range(1,nr_symbols+1):    
#    password += random.choice(symbols)
#    
#for number in range(1, nr_numbers+1):    
#    password+= random.choice(numbers)    
#
#print(password)


## Hard Level - Order of characters randomised.
# Adding values as list.
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password = [] # setup

for letter in range(1,nr_letters+1):
    password.append(random.choice(letters))

for symbol in range(1,nr_symbols+1):
    password.append(random.choice(symbols))
    
for number in range(1, nr_numbers+1):
    password.append(random.choice(numbers))
    
random.shuffle(password) # Shuffle the password characters
# print(password)

# Concatenate the password characters to string
final_pw = "" # setup

for position in range(1,len(password)+1):
  final_pw = final_pw + password[position-1]

print(f"Your password is: {final_pw}")

