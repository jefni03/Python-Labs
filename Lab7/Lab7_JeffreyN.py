# text = "python is an easy language python is easy to learn and easy to code a lot of python modules that are easy to use go python"

# keys = text.split()

# value = {}
# for word in keys:
#     if word not in value:
#         value[word] = 1
#     else:
#         value[word] += 1

# for word, freq in value.items():
#     print(word, freq)

# top_words = sorted(value.items(), key=lambda x: x[1], reverse=True)[:3]

# print("The 3 most frequent words are:")
# for word, freq in top_words:
#     print(word, freq)

# text = "i enjoy playing guitar and basketball and basketball is a sport and guitar is an instrument that is able to make nice sounds basketball are able to bounce and people shoot them into a basket which is attached to a backboard and there is a net basketball is fun and i enjoy it "

# keys = text.split()

# value = {}
# for word in keys:
#     if word not in value:
#         value[word] = 1
#     else:
#         value[word] += 1

# for word, freq in value.items():
#     print(word, freq)

# top_words = sorted(value.items(), key=lambda x: x[1], reverse=True)[:3]

# print("The 3 most frequent words are:")
# for word, freq in top_words:
#     print(word, freq)

text = "i want to go to japan during the summer japan has many beautiful views and places to explore japan has a unique and fun culture japan has good food and many small shops to explore japan is advanced in their technology and i want to see everything japan will be fun"

keys = text.split()

value = {}
for word in keys:
    if word not in value:
        value[word] = 1
    else:
        value[word] += 1

for word, freq in value.items():
    print(word, freq)

top_words = sorted(value.items(), key=lambda x: x[1], reverse=True)[:3]

print("The 3 most frequent words are:")
for word, freq in top_words:
    print(word, freq)

'''
Results:
python 4
is 2
an 1
easy 4
language 1
to 3
learn 1
and 1
code 1
a 1
lot 1
of 1
modules 1
that 1
are 1
use 1
go 1
The 3 most frequent words are:
python 4
easy 4
to 3

i 2
enjoy 2
playing 1
guitar 2
and 6
basketball 4
is 6
a 4
sport 1
an 1
instrument 1
that 1
able 2
to 3
make 1
nice 1
sounds 1
are 1
bounce 1
people 1
shoot 1
them 1
into 1
basket 1
which 1
attached 1
backboard 1
there 1
net 1
fun 1
it 1
The 3 most frequent words are:
and 6
is 6
basketball 4

i 2
want 2
to 5
go 1
japan 6
during 1
the 1
summer 1
has 3
many 2
beautiful 1
views 1
and 4
places 1
explore 2
a 1
unique 1
fun 2
culture 1
good 1
food 1
small 1
shops 1
is 1
advanced 1
in 1
their 1
technology 1
see 1
everything 1
will 1
be 1
The 3 most frequent words are:
japan 6
to 5
and 4
'''

# Task 2
import random

L1 = [random.randint(1, 100) for i in range(100)]
L2 = [i for i in range(1, 101) if i % 3 == 0 or i % 4 == 0]
S1 = set(L1)
S2 = frozenset(L2)
R1 = S1.union(S2)
print("There are " + str(len(R1)) + " elements in R1")
R2 = S1.intersection(S2)
print("There are " + str(len(R2)) + " elements in R2")
R3 = S1.difference(S2)
print("There are " + str(len(R3)) + " elements in R3")

'''
Results:
There are 77 elements in R1
There are 36 elements in R2
There are 27 elements in R3
'''