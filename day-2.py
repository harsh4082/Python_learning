

'''
1. Control Flow: If-Else Statements
Control flow allows your program to make decisions based on conditions.
'''

age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
elif age == 18:
    print("You just became an adult!")
else:
    print("You are an adult.")

'''
2. Logical and Comparison Operators
Comparison Operators: Used to compare values.

== (equal), != (not equal), < (less than), > (greater than), <= (less than or equal to), >= (greater than or equal to).
Logical Operators: Combine conditions.

and: True if both conditions are True.
or: True if at least one condition is True.
not: Reverses the condition.
'''

a = 10
b = 20

if a < b and b > 15:
    print("Both conditions are True")
if a > b or b > 15:
    print("At least one condition is True")
if not a == b:
    print("a and b are not equal")

'''
3. Loops
For Loop
Used to iterate over a sequence (like a list, string, or range).
'''
for i in range(1, 6):  # Loops from 1 to 5
    print(f"Number: {i}")

'''
While Loop
Runs as long as a condition is True.
'''
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1  # Increment the count

'''
4. Practice Exercises
1)  Simple If-Else: Write a program to check if a number entered by the user is even or odd.
'''

num1 = int(input("Enter a Number: "))

if num1%2 == 0 :
    print("Even Number")
else:
    print("Odd Number")

'''
Grade Calculator:

Take a number as input (marks).
Print:
"A" if marks >= 90
"B" if marks >= 80 and < 90
"C" if marks >= 60 and < 80
"Fail" if marks < 60.
'''

marks = int(input("Enter a Number: "))

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("Fail")


'''
Number Guessing Game:

Use a while loop to let the user guess a number between 1 and 10.
Print "Correct!" if the user guesses the number (e.g., 5), and "Try Again" otherwise.
'''

# count = 0
# while count <= 10:
#     print(f'count {count}')
#     count += 1

# Secret number to guess
secret_number = 5  

# Start the game
print("Guess the number between 1 and 10!")

while True:  # Infinite loop; will break when the user guesses correctly
    # Take input from the user
    user_guess = int(input("Enter your guess: "))
    
    # Check if the guess is correct
    if user_guess == secret_number:
        print("Correct! You guessed the right number!")
        break  # Exit the loop
    else:
        print("Try Again!")


# Number Guessing Game
import random
secret_number = random.randint(1, 10)  # Generates a random number between 1 and 10
print("Guess the number between 1 and 10!")

while True:
    user_guess = int(input("Enter your guess: "))
    if 1 <= user_guess <= 10:
        if user_guess == secret_number:
            print("Correct! You guessed the right number!")
            break
        else:
            print("Try Again!")
    else:
        print("Please enter a number between 1 and 10.")