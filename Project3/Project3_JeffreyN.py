import os
import string
from collections import Counter
import random


def is_valid(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in string.punctuation for char in password):
        return False
    return True

def login_user(dictionary):
    tries = 0
    while tries < 3:
        username = input("Enter username: ")
        if username in dictionary:
            password = input("Enter password: ")
            if password == dictionary[username]:
                print("Login is successful")
                return True
            else:
                print("Incorrect. Please try again")
        else:
            print("Username not found. Please try again")
        tries += 1
    print("Fail. Too many attempts")
    return False

def create_user(dictionary):
    tries = 0
    while tries < 3:
        newname = input("Enter a new username: ")
        if not newname.isalpha():
            print("Username must contain only letters. No symbols etc.")
            tries += 1
            continue
        if newname in dictionary:
            print("Username already exists")
            tries += 1
            continue
        new_password = input("Enter a new password: ")
        if not is_valid(new_password):
            print("Password must be at least 8 characters and contain at least one lowercase letter, one uppercase letter, one digit, and one special character.")
            tries += 1
            continue
        dictionary[newname] = new_password
        print("Welcome, {}!".format(newname))
        return newname
    print("Fail. Too many attempts")
    return None

def update_password(dictionary, usernames):
    if not login_user(dictionary):
        return False
    new_password = input("Enter a new password: ")
    if not is_valid(new_password):
        print("Password must be at least 8 characters and contain at least one lowercase letter, one uppercase letter, one digit, and one special character.")
        return False
    dictionary[usernames] = new_password
    print("Password is now updated")
    return True

def main():
    usernames = ['lyang', 'kSimon', 'danny', 'tomatcpp', 'csDept', 'CoScpp', 'broncoWins', 'ponyExp', 'BldgAndRooms', 'helloKitty']
    passwords = ['sheCodes#123', 'catchAllGood1%', '@my2Choices', '123abc;;;', 'Hello2Monday$', 'GoodFriday@Cpp2', 'CS2520@Python', 'JavaIsHot2!', '2ManyRainingDays!', '1Startup@Starbucks']
    dictionary = dict(zip(usernames, passwords))
    login_user(dictionary)
    create_user(dictionary)
    update_password(dictionary, usernames)

if __name__ == '__main__':
    main()

'''
Results:
Enter username: bob
Username not found. Please try again
Enter username: lyang
Enter password: 123
Incorrect. Please try again
Enter username: 123
Username not found. Please try again
Fail. Too many attempts
Enter a new username: bob
Enter a new password: 123
Password must be at least 8 characters and contain at least one lowercase letter, one uppercase letter, one digit, and one special character.
Enter a new username: bob
Enter a new password: 1234
Password must be at least 8 characters and contain at least one lowercase letter, one uppercase letter, one digit, and one special character.       
Enter a new username: bob
Enter a new password: 1234
Password must be at least 8 characters and contain at least one lowercase letter, one uppercase letter, one digit, and one special character.       
Fail. Too many attempts

Enter username: lyang
Enter password: sheCodes#123
Login is successful
Enter a new username: Jeffrey
Enter a new password: heCodes#123
Welcome, Jeffrey!
Enter username: danny 
Enter password: @my2Choices
Login is successful
Enter a new password: #heCodes123
Password is now updated

Enter username: lyang
Enter password: sheCodes#123
Login is successful
Enter a new username: Jeffrey
Enter a new password: #heCodes123
Welcome, Jeffrey!
Enter username: bob
Username not found. Please try again
Enter username: danny
Enter password: @my2Choices
Login is successful
Enter a new password: 213
Password must be at least 8 characters and contain at least one lowercase letter, one uppercase letter, one digit, and one special character. 
'''

# Task 2
def read_files(file_name):
    while True:
        try:
            with open(file_name, 'r') as file:
                lines = file.readlines()
                list = []
                for line in lines:
                    words = line.lower().split()
                    proper_words = []
                    for word in words:
                        proper_word = word.strip(string.punctuation)
                        if proper_word.isalpha():
                            proper_words.append(proper_word)
                    list.append(proper_words)
                return list
        except FileNotFoundError:
            print(file_name, "not found. Please reenter")
            file_name = input("Enter filename: ")

# Reads the two text files and puts into list 
file1 = input("Enter file 1 name: ")
file2 = input("Enter file 2 name: ")
file1_lines = read_files(file1)
file2_lines = read_files(file2)
file1_words = [word for line in file1_lines for word in line]
file2_words = [word for line in file2_lines for word in line]

# print number of lines and words for the files 
file1_lines_number = len(file1_lines)
file1_words_number = len(file1_words)
file2_lines_number = len(file2_lines)
file2_words_number = len(file2_words)
print(file1_lines_number)
print(file1_words_number)
print(file2_lines_number)
print(file2_words_number)

file1_set = set(file1_words)
file2_set = set(file2_words)

# Calculate set operations
total = len(file1_set.union(file2_set))
common = len(file1_set.intersection(file2_set))
file1_exclusive = len(file1_set.difference(file2_set))
file2_exclusive = len(file2_set.difference(file1_set))
unique_words = len(file1_set.symmetric_difference(file2_set))

# Print results
print(f"{file1_lines} lines and {file1_words} words in {file1}")
print(f"{file2_lines} lines and {file2_words} words in {file2}")
print(f"{total} distinct words used in the two files")
print(f"{common} words appear in both files")
print(f"{file1_exclusive} words appear in {file1} only and not in {file2}.")
print(f"{file2_exclusive} words appear in {file2} only and not in {file1}.")
print(f"{unique_words} words not repeated in both articles.")

# Word frequency counter
word_count = Counter(file1_words + file2_words)
sorted = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
print("Word frequency count:")
for word, count in sorted:
    print(f"{word}: {count}")

'''
Results:
Enter file 1 name: Python.txt
Enter file 2 name: MachineLearning.txt
8
78
4
49
[['python', 'is', 'a', 'high', 'level', 'general', 'purpose', 'programming', 'language'], ['the', 'design', 'philosophy', 'of', 'python', 'emphasizesâ', 'code', 'readability'], ['python', 'consistently', 'ranks', 'as', 'one', 'of', 'the', 'most', 'popular', 'programming', 'languages'], ['machine', 'learning', 'is', 'a', 'field', 'of', 'computer', 'science', 'that', 'uses', 'statistical', 'techniques'], ['to', 'give', 'computer', 'programs', 'the', 'ability', 'to', 'learn', 'from', 'past', 'experiences'], ['and', 'improve', 'how', 'they', 'perform', 'specific', 'tasks'], ['you', 'will', 'learn', 'the', 'steps', 'necessary', 'to', 'create', 'a', 'successful', 'machine', 'learning', 'application'], ['with', 'python', 'and', 'the', 'scikit', 'learn', 'library']] lines and ['python', 'is', 'a', 'high', 'level', 'general', 'purpose', 'programming', 'language', 'the', 'design', 'philosophy', 'of', 'python', 'emphasizesâ', 'code', 'readability', 'python', 'consistently', 'ranks', 'as', 'one', 'of', 'the', 'most', 'popular', 'programming', 'languages', 'machine', 'learning', 'is', 'a', 'field', 'of', 'computer', 'science', 'that', 'uses', 'statistical', 'techniques', 'to', 'give', 'computer', 'programs', 'the', 'ability', 'to', 'learn', 'from', 'past', 'experiences', 'and', 'improve', 'how', 'they', 'perform', 'specific', 'tasks', 'you', 'will', 'learn', 'the', 'steps', 'necessary', 'to', 'create', 'a', 'successful', 'machine', 'learning', 'application', 'with', 'python', 'and', 'the', 'scikit', 'learn', 'library'] words in Python.txt
[['learning', 'is', 'making', 'the', 'computer', 'learn', 'from', 'studying', 'data', 'and', 'statistics'], ['machine', 'learning', 'is', 'a', 'step', 'into', 'the', 'direction', 'of', 'artificial', 'intelligence'], ['machine', 'learning', 'is', 'a', 'program', 'that', 'analyses', 'data', 'and', 'learns', 'to', 'predict', 'the', 'outcome'], ['get', 'ready', 'to', 'dive', 'into', 'the', 'world', 'of', 'machine', 'learning', 'by', 'using', 'python']] lines and ['learning', 'is', 'making', 'the', 'computer', 'learn', 'from', 'studying', 'data', 'and', 'statistics', 'machine', 'learning', 'is', 'a', 'step', 'into', 'the', 'direction', 'of', 'artificial', 'intelligence', 'machine', 'learning', 'is', 'a', 'program', 'that', 'analyses', 'data', 'and', 'learns', 'to', 'predict', 'the', 'outcome', 'get', 'ready', 'to', 'dive', 'into', 'the', 'world', 'of', 'machine', 'learning', 'by', 'using', 'python'] words in MachineLearning.txt
77 distinct words used in the two files
13 words appear in both files
44 words appear in Python.txt only and not in MachineLearning.txt.
20 words appear in MachineLearning.txt only and not in Python.txt.
64 words not repeated in both articles.
Word frequency count:
the: 9
learning: 6
python: 5
is: 5
a: 5
of: 5
machine: 5
to: 5
learn: 4
and: 4
computer: 3
programming: 2
that: 2
from: 2
data: 2
into: 2
high: 1
level: 1
general: 1
purpose: 1
language: 1
design: 1
philosophy: 1
emphasizesâ: 1
code: 1
readability: 1
consistently: 1
ranks: 1
as: 1
one: 1
most: 1
popular: 1
languages: 1
field: 1
science: 1
uses: 1
statistical: 1
techniques: 1
give: 1
programs: 1
ability: 1
past: 1
experiences: 1
improve: 1
how: 1
they: 1
perform: 1
specific: 1
tasks: 1
you: 1
will: 1
steps: 1
necessary: 1
create: 1
successful: 1
application: 1
with: 1
scikit: 1
library: 1
making: 1
studying: 1
statistics: 1
step: 1
direction: 1
artificial: 1
intelligence: 1
program: 1
analyses: 1
learns: 1
predict: 1
outcome: 1
get: 1
ready: 1
dive: 1
world: 1
by: 1
using: 1

Enter file 1 name: kevin
Enter file 2 name: lebron
kevin not found. Please reenter
Enter filename: kevin.txt
lebron not found. Please reenter
Enter filename: lebron.txt
2
51
2
53
[['kevin', 'wayne', 'durant', 'also', 'known', 'by', 'his', 'initials', 'kd', 'is', 'an', 'american', 'professional', 'basketball', 'player', 'for', 'the', 'phoenix', 'suns', 'of', 'the', 'national', 'basketball', 'association'], ['he', 'played', 'one', 'season', 'of', 'college', 'basketball', 'for', 'the', 'texas', 'longhorns', 'and', 'was', 'selected', 'as', 'the', 'second', 'overall', 'pick', 'by', 'the', 'seattle', 'supersonics', 'in', 'the', 'nba', 'draft']] lines and ['kevin', 'wayne', 'durant', 'also', 'known', 'by', 'his', 'initials', 'kd', 'is', 'an', 'american', 'professional', 'basketball', 'player', 'for', 'the', 'phoenix', 'suns', 'of', 'the', 'national', 'basketball', 'association', 'he', 'played', 'one', 'season', 'of', 'college', 'basketball', 'for', 'the', 'texas', 'longhorns', 'and', 'was', 'selected', 'as', 'the', 'second', 'overall', 'pick', 'by', 'the', 'seattle', 'supersonics', 'in', 'the', 'nba', 'draft'] words in kevin
[['lebron', 'raymone', 'james', 'sr', 'is', 'an', 'american', 'professional', 'basketball', 'player', 'for', 'the', 'los', 'angeles', 'lakers', 'in', 'the', 'national', 'basketball', 'association'], ['nicknamed', 'king', 'james', 'he', 'is', 'considered', 'to', 'be', 'one', 'of', 'the', 'greatest', 'basketball', 'players', 'in', 'history', 'and', 'is', 'often', 'compared', 'to', 'michael', 'jordan', 'in', 'debates', 'over', 'the', 'greatest', 'basketball', 'player', 'of', 'all', 'time']] lines and ['lebron', 'raymone', 'james', 'sr', 'is', 'an', 'american', 'professional', 'basketball', 'player', 'for', 'the', 'los', 'angeles', 'lakers', 'in', 'the', 'national', 'basketball', 'association', 'nicknamed', 'king', 'james', 'he', 'is', 'considered', 'to', 'be', 'one', 'of', 'the', 'greatest', 'basketball', 'players', 'in', 'history', 'and', 'is', 'often', 'compared', 'to', 'michael', 'jordan', 'in', 'debates', 'over', 'the', 'greatest', 'basketball', 'player', 'of', 'all', 'time'] words in lebron
64 distinct words used in the two files
15 words appear in both files
26 words appear in kevin only and not in lebron.
23 words appear in lebron only and not in kevin.
49 words not repeated in both articles.
Word frequency count:
the: 10
basketball: 7
is: 4
of: 4
in: 4
player: 3
for: 3
by: 2
an: 2
american: 2
professional: 2
national: 2
association: 2
he: 2
one: 2
and: 2
james: 2
to: 2
greatest: 2
kevin: 1
wayne: 1
durant: 1
also: 1
known: 1
his: 1
initials: 1
kd: 1
phoenix: 1
suns: 1
played: 1
season: 1
college: 1
texas: 1
longhorns: 1
was: 1
selected: 1
as: 1
second: 1
overall: 1
pick: 1
seattle: 1
supersonics: 1
nba: 1
draft: 1
lebron: 1
raymone: 1
sr: 1
los: 1
angeles: 1
lakers: 1
nicknamed: 1
king: 1
considered: 1
be: 1
players: 1
history: 1
often: 1
compared: 1
michael: 1
jordan: 1
debates: 1
over: 1
all: 1
time: 1
'''