'''
1. What is Python?
Python is a versatile, high-level programming language used in web development, data science, automation, and more. It's known for its simplicity and readability.
'''

print("Hello, World!")


'''
Variables and Data Types
Python variables are used to store data. You don't need to declare their type; Python figures it out for you.
'''

name = "John"  # String
age = 25       # Integer
height = 5.8   # Float
is_student = True  # Boolean

print(name)
print(age)
print(height)
print(is_student)

'''
Taking Input
Use the input() function to get data from the user.
'''
name = input("What is your name? ")
print("Hello, " + name + "!")

color = input("What is your favorite color? ")
print(f"Wow, {color} is a great choice!")

#Basic Arithmetic
a = 5
b = 3
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus (remainder)

#Basic Arithmetic with input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("The sum is:", num1 + num2)


'''Your Practice for Today
Write a program to print your name, age, and city.
Take input for two numbers and print:
Their sum.
Their product.
Their difference.'''

# name1 = str(input("Enter your name: "))
name1 = (input("Enter your name: "))
age = int(input("Enter your age: "))
# city = str(input("Enter your city: "))
city = (input("Enter your city: "))

# print("Hello My name is ", name1 ,"and i am ",age,"years old and i live in",city)
print(f"Hello! My name is {name1}, I am {age} years old, and I live in {city}.")

num3 = int(input("enter first number: "))
num4 = int(input("enter second number: "))

sumofnumber = num3 + num4
product = num3 * num4
difference = num3 - num4

# print("the sum of ",num3," and ",num4," is ",sumofnumber)
# print("the product of ",num3," and ",num4," is ",product)
# print("the difference of ",num3," and ",num4," is ",difference)

# Printing the results
print(f"The sum of {num3} and {num4} is {sumofnumber}.")
print(f"The product of {num3} and {num4} is {product}.")
print(f"The difference between {num3} and {num4} is {difference}.")
