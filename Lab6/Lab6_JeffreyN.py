import random

# Task 1
input = input("Please enter a sentence: ")
print("Here is your input", input)
sequence = input.split()
print("String split:", sequence)
for i in sequence:
    print(i + "#", end = "")
'''
Results:
Please enter a sentence: Good Morning CS2520
Here is your input Good Morning CS2520
String split: ['Good', 'Morning', 'CS2520']
Good#Morning#CS2520#

Please enter a sentence: I enjoy playing basketball 
Here is your input I enjoy playing basketball
String split: ['I', 'enjoy', 'playing', 'basketball']
I#enjoy#playing#basketball#
'''

# Task 2
list = []
special_character = '#'
while True:
    user_input = input("please enter integers for a list and enter # when you are done: ")
    if user_input == special_character:
        break
    else:
        list.append(int(user_input))
print(list)

list2 = [random.randint(0, 50) for _ in range(20)]
print(list2)

print(list[-1])
print(list[::-1])

combine = list + list2
combine.sort(reverse = True)
print(combine)
'''
Results:
please enter integers for a list and enter # when you are done: 5
please enter integers for a list and enter # when you are done: 2
please enter integers for a list and enter # when you are done: 21
please enter integers for a list and enter # when you are done: 23
please enter integers for a list and enter # when you are done: 13
please enter integers for a list and enter # when you are done: 17
please enter integers for a list and enter # when you are done: 8
please enter integers for a list and enter # when you are done: 1
please enter integers for a list and enter # when you are done: 12
please enter integers for a list and enter # when you are done: 45
please enter integers for a list and enter # when you are done: #
[5, 2, 21, 23, 13, 17, 8, 1, 12, 45]
[17, 14, 35, 25, 9, 17, 7, 37, 29, 2, 8, 3, 13, 5, 19, 35, 29, 30, 45, 2]
45
[45, 12, 1, 8, 17, 13, 23, 21, 2, 5]
[45, 45, 37, 35, 35, 30, 29, 29, 25, 23, 21, 19, 17, 17, 17, 14, 13, 13, 12, 9, 8, 8, 7, 5, 5, 3, 2, 2, 2, 1]

please enter integers for a list and enter # when you are done: 9
please enter integers for a list and enter # when you are done: 7
please enter integers for a list and enter # when you are done: 29
please enter integers for a list and enter # when you are done: 13
please enter integers for a list and enter # when you are done: 45
please enter integers for a list and enter # when you are done: 54
please enter integers for a list and enter # when you are done: 3
please enter integers for a list and enter # when you are done: 2
please enter integers for a list and enter # when you are done: 5
please enter integers for a list and enter # when you are done: 21
please enter integers for a list and enter # when you are done: 43
please enter integers for a list and enter # when you are done: #
[9, 7, 29, 13, 45, 54, 3, 2, 5, 21, 43]
[35, 27, 17, 8, 10, 28, 46, 31, 40, 32, 10, 11, 30, 43, 12, 15, 5, 7, 2, 46]
43
[43, 21, 5, 2, 3, 54, 45, 13, 29, 7, 9]
[54, 46, 46, 45, 43, 43, 40, 35, 32, 31, 30, 29, 28, 27, 21, 17, 15, 13, 12, 11, 10, 10, 9, 8, 7, 7, 5, 5, 3, 2, 2]
'''
# Task 3

names = ('Winny', 'Ada', 'Lev', 'Kay', 'Jack', 'Sam', 'Mark')
ages = [20, 18, 22, 16, 20, 18, 18]
NameAgePair = tuple(zip(names, ages))
print(NameAgePair)

youngest = min(NameAgePair, key = lambda x: x[1])[0]
print(youngest, "is the youngest")

ages = [x[1] for x in NameAgePair]
average = sum(ages) / len(ages)
print(average, "is the average age")

sorted = sorted(NameAgePair, key=lambda x: (-x[1], x[0]))
print(sorted)

# names = ('Jeffrey', 'Hanjoo', 'Leon', 'George', 'Jasper', 'Glory', 'Dom', 'Matt')
# ages = [19, 18, 21, 21, 19, 18, 24, 22]
# NameAgePair = tuple(zip(names, ages))
# print(NameAgePair)

# youngest = min(NameAgePair, key = lambda x: x[1])[0]
# print(youngest, "is the youngest")

# ages = [x[1] for x in NameAgePair]
# average = sum(ages) / len(ages)
# print(average, "is the average age")

# sorted = sorted(NameAgePair, key=lambda x: (-x[1], x[0]))
# print(sorted)
'''
Results:
(('Winny', 20), ('Ada', 18), ('Lev', 22), ('Kay', 16), ('Jack', 20), ('Sam', 18), ('Mark', 18))
Kay is the youngest
18.857142857142858 is the average age
[('Lev', 22), ('Jack', 20), ('Winny', 20), ('Ada', 18), ('Mark', 18), ('Sam', 18), ('Kay', 16)]

(('Jeffrey', 19), ('Hanjoo', 18), ('Leon', 21), ('George', 21), ('Jasper', 19), ('Glory', 18), ('Dom', 24), ('Matt', 22))
Hanjoo is the youngest
20.25 is the average age
[('Dom', 24), ('Matt', 22), ('George', 21), ('Leon', 21), ('Jasper', 19), ('Jeffrey', 19), ('Glory', 18), ('Hanjoo', 18)]
'''