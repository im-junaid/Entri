# Challenge 1: Basic Arithmetic Operations
"""
Problem:
Write a program that takes two numbers as input and prints the results of the following operations:
Addition
Subtraction
Multiplication
Division
You should calculate and print all results one by one,

Input:
Two numbers (integers or floats)

Output:

Sum of the two numbers
Difference (first number minus second number)
Product of the two numbers
Division (first number divided by the second number)
Example:
Input:
8
4
Output:

Addition: 12
Subtraction: 4
Multiplication: 32
Division: 2.0
"""

# Code :
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num1

print(f"""
Addition : {add}
Subtraction : {sub}
Multiplication : {mul}
Division : {div}
""")
