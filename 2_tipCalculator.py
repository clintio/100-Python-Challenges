#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
# Inputs
print("Welcome to the tip calculator!\n")
total_bill = input("What was the total bill? $")
tip_percent = input("How much tip would you like to give? 10, 12, or 15? ")
number_people = input("How many people to split the bill? ")

#Calculations
tip_decimal = 1 + float(tip_percent)/100
each_person_pay = (float(total_bill)/int(number_people))*tip_decimal

each_person_pay_2decimal = round(each_person_pay, 2)

#Output
print(f"Each person should pay: ${each_person_pay_2decimal}")
