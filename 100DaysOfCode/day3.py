
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 200:
    print("You can ride the rollercoaster")
    age = int(input("What's your age? "))
    if age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

#Challenge 1
check_number = int(input("Please enter your number for check: "))

if check_number % 2 ==0:
    print("This is an even number")
else:
    print("This is an odd number.")


#challenge 2

users_weight = int(input("Please type your weight in kg: "))
users_height = float(input("Please enter your height in m: "))
bmi = round(users_weight/(users_height)**2)
if bmi < 18.5:
    print(f"Your bmi is {bmi},you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese.")
else:
    print(f"Your bmi is {bmi}, you are clinically obese.")
print(bmi)


#Leap Year Challenge
year = int(input("Which year do you want to check?"))

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print ("Leap year.")
        else:
            print ("Not a leap year.")
    else:
        print ("Leap year.")
else:
    print ("Not a leap year.")

#Pizza order challenge

print('Welcome to Python Pizza Deliveries')
size = int(input('What size of pizza do you want? S,M or L? '))
add_pepperoni = input('Do you want pepperoni? Y or N ')
extra_cheese = input('Do you want extra cheese? Y or N ')

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill +=20
else:
    bill +=25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1
print(f'Your total bill is ${bill}.')

#Love Calculator Challenge
print('Welcome to Love Calculator.')
name1 = input('What is your name? \n')
name2 = input('What is their name? \n')
concatenate_string  = name1 + name2
lowercase_string = concatenate_string.lower()

t = lowercase_string.count("t")
r = lowercase_string.count("r")
u = lowercase_string.count("u")
e = lowercase_string.count("e")

true = t + r + u + e

l = lowercase_string.count("l")
o = lowercase_string.count("o")
v = lowercase_string.count("v")
e = lowercase_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score) < 10 or (love_score > 900):
    print(f'Your love score is {love_score}, you go together like coke and mentos.')
elif (love_score >= 40) and (love_score <= 50):
    print(f'Your score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}.')
print(love_score)


#Project 3 Treasure Island
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
print('Welcome to Treasure Island.')
print('Your mission is to find the Treasure. ')
option = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' ")

if option == "left":
    left_option = input("You came to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. \n")
    if left_option == "wait":
        left_option_color = input("You arrive at an island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n")
        if left_option_color == "red":
            print('Game Over!')
        elif left_option_color == "yellow":
            print('You Win!')
        else:
            print("You enter a room of beasts. Game Over!")
    else:
        print("Game Over!")
                
else:
    print("Game Over!")
