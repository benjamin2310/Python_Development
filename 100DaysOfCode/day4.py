import random
#import my_module

random_integer = random.randint(1,100)
print(random_integer)

#print(my_module.pi)

random_float = random.random() * 5
print(random_float)

random_decimal = random.uniform(0,5)
print(random_decimal)


#challenge 1
import random

the_number = random.randint(0,1)

if the_number == 1:
    print("Heads!")
else:
    print("Tails!")

#challenge 2
import random
names_string = input("Give me everbody's names, separated by a comma.")

names = names_string.split(", ")

num_items = len(names)
random_choice = random.randint(0, num_items - 1)
#Fix this error
#person_who_will_pay = names[random_choice]
person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to pay for the meal today.")


#challenge 3 on list

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")


horizontal = int(position[0])
vertical = int(position[1])


selected_row = (map[vertical - 1])
selected_row[horizontal - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")


#Peoject for day 4
import random

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
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
