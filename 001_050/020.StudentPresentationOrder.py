# student presentation order.

# import the function to shuffle a list.
from random import shuffle

# ask for the names of the four students.
student1 = input("Enter the first student's name: ")
student2 = input("Enter the second student's name: ")
student3 = input("Enter the third student's name: ")
student4 = input("Enter the fourth student's name: ")

# create a list with all four students.
students = [student1, student2,student3,student4]

# shuffe the presentation order.
shuffle(students)

# show each student in the new order.
for student in students:
 print(student) 