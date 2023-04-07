# Authors: Jeffrey Ni 
# Assignment: Lab #4
# Completed (or last revision):  02/16/2023

import math
# Task 1
print(sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))
print(math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1]))
'''
Result:
0.9999999999999999
1.0

The results are different because fsum is more precise. 
'''

# Task 2
def task2() :
    for i in range (8) :
        print(i, end = ' ')
print(task2())
'''
Result:
0 1 2 3 4 5 6 7 None

It prints None because print(task2()) is used instead of just task2(). It is trying to print task2's return value, but there is none.
'''

# Task 3
def fun (x = 1, y = 2, z):
    z = x + y
    y += 1
    return z*y
fun(3,z=5)
'''
a. There is an error because the arugment of z is not defined and all positional arguments go first
b. if there was no error, the result would be 15

'''
def hoho (x, y = 2, z=1):
    z = x + z
    y += 1
    return z*y
hoho(5)
hoho(6,z=3,y=1)
'''
The header line of the function is correct and there is no error. 
The result of both function calls would be 18. 
'''

# Task 4

def swap(a, b):
     a, b = b, a
     return (a, b)
def main () :
     z = int(input("Enter first integer to swap: "))
     y = int(input("Enter Second integer to swap: "))
     print(swap(z, y))

main()
'''
It will not swap because x is not defined.
Results:
Enter first integer to swap: 4
Enter Second integer to swap: 3
(3, 4)
Enter first integer to swap: 2
Enter Second integer to swap: 5
(5, 2)

'''
# Task 5
a, b = 0, 5
def main() :
    global a, b
    i = 10
    b = g(i)
    print(a+b+i)
def f(i) :
    n=0
    while n*n <= i:
        n = n + 1
    return n-1
def g(a) :
    b=0
    for n in range(a):
        i = f(n)
        b = b+i
        return b

main()

'''
a and b are global variables while i, b, and n are all local variables. 
I think that the program will print out 10.
My guess was correct. 

'''