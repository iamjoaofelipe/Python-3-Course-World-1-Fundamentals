# student name draw.

# import the function to choose a random name.
from random import choice

# ask for the names of the four students.
student1 = input("Enter the first student's name: ")
student2 = input("Enter the second student's name: ") 
student3 = input("Enter the third student's name: ")
student4 = input("Enter the fourth student's name: ")

# create a list with all four students.
students = [student1, student2,student3,student4]

# choose one student randomly. 
chosen_student = choice(students)

# show the name of the chosen student.
print("the chosen student is:", chosen_student) 