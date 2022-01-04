# Source- https://www.udemy.com/course/100-days-of-code/learn/lecture/18029131#overview  
# My code- https://replit.com/@clintio/tip-calculator-start#main.py  

## Python script  
# Calculate how much everyone owes if the bill is
# $150.00 total
# Split between 5 people 
# 12% tip 

#Each person should pay ($150.00 / 5 people) * 1.12 tip = $33.6  
#Format the result to 2 decimal places = $33.60

#Tip: There are 2 ways to round a number. 

#Inputs  
print("Welcome to the tip calculator!\n")  
total_bill = float(input("What was the total bill? $"))  
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))  
number_people = int(input("How many people to split the bill? "))  

#Calculations  
tip_decimal = 1 + tip_percent/100  
each_person_pay = (total_bill/number_people)*tip_decimal

each_person_pay_2decimal = "{:.2f}".format(each_person_pay)

#Output  
print(f"Each person should pay: ${each_person_pay_2decimal}")
