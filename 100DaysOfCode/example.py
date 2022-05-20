scores = [78,65,89,86,55,91,64,90,89]

higest_score = 0
for score in scores:
        if score > higest_score:
            highest_score = score
print(f"The highest score in the class is: {highest_score}")

cars = ["Bmw","Benz","Toyota","Honda"]

for car in cars:
    print(car)


##check these codes again


#challenge 1
student_heights = input('Input a list of students height ').split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights)
print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)



number_of_students = len(student_heights)
average_height = round(total_height / number_of_students)
print(average_height) 


#Challenge 2

student_scores = input('Input a list of students height ').split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores)
print(student_scores)

higest_score = 0
for score in student_scores:
        if score > higest_score:
            highest_score = score
print(f"The highest score in the class is: {higest_score}")

import string

letters = 'x'