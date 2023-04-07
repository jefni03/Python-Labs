# Authors: Jeffrey Ni 
# Assignment: Lab #3
# Completed (or last revision):  02/11/2023

# Task 1
test_run = int(input("Enter 1, 2, or 3 if your three input are string, integers, or float numbers, respectively: "))
if test_run == 1:
    first_value = input("Enter first string: ")
    second_value = input("Enter second string: ")
    third_value = input("Enter third string: ")
elif test_run == 2:
    first_value = int(input("Enter first integer: "))
    second_value = int(input("Enter second integer: "))
    third_value = int(input("Enter third integer: "))
else:
    first_value = float(input("Enter first float number: "))
    second_value = float(input("Enter second float number: "))
    third_value = float(input("Enter third float number: "))
if first_value > second_value and first_value > third_value:
        largest = first_value
elif second_value > first_value and second_value > third_value:
        largest = second_value
else:
        largest = third_value
print("The largest of the three values is", str(largest))

'''
Results:
Enter 1, 2, or 3 if your three input are string, integers, or float numbers, respectively: 1
Enter first string: hello
Enter second string: how're you
Enter third string: hoho
The largest of the three values is how're you

Enter 1, 2, or 3 if your three input are string, integers, or float numbers, respectively: 2
Enter first integer: 420
Enter second integer: 351
Enter third integer: 530
The largest of the three values is 530

Enter 1, 2, or 3 if your three input are string, integers, or float numbers, respectively: 3
Enter first float number: -35.8
Enter second float number: -28
Enter third float number: -36.5
The largest of the three values is -28.0
'''
   
# Task 2
count = int(input("please enter the number of items purchased "))
total = int(input("please enter the total cost "))
print("Average =", "0" if count == 0 else total/count)

'''
Results:
please enter the number of items purchased 3
please enter the total cost 15
Average = 5.0

please enter the number of items purchased 0
please enter the total cost 15
Average = 0
'''

# Task 3
j=1
while j < 10 :
      j += 2
      if j == 5 :
            continue
      print(j, end =  " ")
'''
a. I thought it was going to print 3 7 9 11 and I was correct
b. The actual output was 3 7 9 11
c. My guess was the same as the actual output 
'''
for j in range (50) :
               j += 2
               print(j, end =  " ")
               if j == 15 :
                      break
'''
a. I think it was going to keep printing until 50 by 2
b. The actual output waas 2 3 4 5 6 7 8 9 10 11 12 13 14 15
c. My guess was not the same as the actual output and it should be brought to attention that j += 2 only runs once. 
'''

# Task 4
input_number = int(input("Enter a Number to check Prime or Not "))
i = 2
count = 0
while i <= input_number/2 :
    if input_number % i == 0:
        count += 1
        break
    i += 1
if count == 0:
    print(str(input_number), "is a prime number")
else:
    print(str(input_number), "is not a prime number")

'''
Results:
Enter a Number to check Prime or Not 71
71 is a prime number

Enter a Number to check Prime or Not 119
119 is not a prime number

Enter a Number to check Prime or Not 45
45 is not a prime number

Enter a Number to check Prime or Not 56
56 is not a prime number

Enter a Number to check Prime or Not 67
67 is a prime number
'''

