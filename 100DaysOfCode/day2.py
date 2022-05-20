from typing import Text


username = "Ben"
my_age = 24
unit_price = 22.4

True 
False

#Challenge 1
user_input = input("Enter your two digit number: ")
first_input = int(user_input[0])
second_input = int(user_input[1])
result = first_input + second_input
print(result)

#Challenge 2

users_weight = int(input("Please type your weight in kg: "))
users_height = float(input("Please enter your height in m: "))
bmi = int(users_weight/(users_height)**2)
print(bmi)

#Project 3

print("Welcome to tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 50? "))
number_of_split = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100 
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / number_of_split
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")

#challenge 4
current_age = int(input("What's you current age? "))
number_of_years = 90 - current_age
number_of_days = number_of_years * 365
number_of_weeks = number_of_years * 52
number_of_months = number_of_years * 12

message = f"You have {number_of_days} days, {number_of_weeks}  weeks, and {number_of_months} months left."
print(message)
