# Authors: Jeffrey Ni 
# Assignment: Lab #2
# Completed (or last revision):  02/06/2023

# Task 1
present_value = float(input("enter present value "))
interest_rate = float(input("enter interest rate "))
years = int(input("enter years "))
print("The future value is" , round(float(present_value*(1+interest_rate/100)**years) , 2))

'''
enter present value 1000.0
enter interest rate 5.0
enter years 30
The future value is 4321.94
'''

# Task 2
v1, v2, v3 = 5, 2, 1
v1+=1
v3 += v1 * v2 - 1 
print(v1, v2, v3)

# 6 2 12

first = input("enter first integer ")
second = input("enter second integer ")
third = input("enter third integer ")
first, second, third = second, third, first
print(first, second, third)

'''
enter first integer 5
enter second integer 7
enter third integer 2
7 2 5
'''

# Task 3
num1 = int(input("enter value of num1 "))
num2 = int(input("enter value of num2 "))
quotient = int(num1/num2)
remainder = num1 % num2
print("quotient when " + str(num1) + " / " + str(num2) + " is " + str(quotient))
print("remainder when " + str(num1) + " is divided by " + str(num2) + " is " + str(remainder))

'''
enter value of num1 12
enter value of num2 35
quotient when 12 / 35 is 0
remainder when 12 is divided by 35 is 12
'''