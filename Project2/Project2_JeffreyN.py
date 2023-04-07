# Authors: Jeffrey Ni 
# Assignment: Project #2
# Completed (or last revision):  03/07/2023


# Task 1

def get_num_of_characters(word):
        count = 0
        for i in word:
                count = count + 1
        return count

def output_without_whitespace(word):
        word = word.replace(" ", "")
        word = word.replace("\t", "")
        return word

def get_safe(word):
    key = "bpzhgocvjdqswkimlutneryaxf"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted_word = ""
    for letter in word:
        if letter.lower() in alphabet:
            encrypted_word += key[alphabet.find(letter.lower())]
        else:
            encrypted_word += letter
    return encrypted_word

def go_recover(word):
      key = "bpzhgocvjdqswkimlutneryaxf"
      alphabet = "abcdefghijklmnopqrstuvwxyz"
      decrypted_word = ""
      for letter in word:
          if letter.lower() in key:
            decrypted_word += alphabet[key.find(letter.lower())]
          else:
            decrypted_word += letter
      return decrypted_word

def main():
        input_value = input('Enter a sentence or phrase: ')
        print("You entered: " + input_value)
        print("Number of characters: " + str(get_num_of_characters(input_value)))
        print("String with no whitespace: " + str(output_without_whitespace(input_value)))
        print("Here is your encypted message using substitution cypher: " + str(get_safe(input_value)))
        print("Here is your decrypted message using substitution cypher: " + str(go_recover(get_safe(input_value))))
if __name__ == '__main__':
        main()

'''
Results: 
Enter a sentence or phrase: The only thing we have to fear is fear itself.
You entered: The only thing we have to fear is fear itself.
Number of characters: 46
String with no whitespace: Theonlythingwehavetofearisfearitself.
Here is your encypted message using substitution cypher: nvg iksx nvjkc yg vbrg ni ogbu jt ogbu jntgso.
Here is your decrypted message using substitution cypher: the only thing we have to fear is fear itself.

Enter a sentence or phrase: My favorite sport is basketball.
You entered: My favorite sport is basketball.
Number of characters: 32
String with no whitespace: Myfavoritesportisbasketball.
Here is your encypted message using substitution cypher: wx obriujng tmiun jt pbtqgnpbss.
Here is your decrypted message using substitution cypher: my favorite sport is basketball.

Enter a sentence or phrase: I play the guitar.
You entered: I play the guitar.
Number of characters: 18
String with no whitespace: Iplaytheguitar.
Here is your encypted message using substitution cypher: j msbx nvg cejnbu.
Here is your decrypted message using substitution cypher: i play the guitar.
'''

# Task 2
import time
import math

def primes(num):
    if num < 2:
        return False
    for i in range(2, int(math.pow(num, 0.5)) + 1):
        if num % i == 0:
            return False
    return True

def generator():
    num = 2
    while True:
        if primes(num):
            yield num
        num += 1

def main():
    prime_digits = []
    prime_gen = generator()
    for i in range(50):
        prime_digits.append(next(prime_gen))
    print("50 prime numbers:" + str(prime_digits))

    prime_gen = generator()
    for i in range(50):
        next(prime_gen)
    start = time.time()
    for i in range(1000):
        prime = next(prime_gen)
        if i == 0:
            first = prime
        elif i == 999:
            last = prime
    end = time.time()
    print("Skip 50 then print one: " + str(first))
    print("Last prime: " + str(last))
    print("Time efficiency: " + str(round(end - start, 4)) +  "secs")

if __name__ == "__main__":
    main()

'''
Results:
50 prime numbers:[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229]
Skip 50 then print one: 233
Last prime: 8387
Time efficiency: 0.016secs
'''

# Task 3
import turtle

def draw(num):
      turtle.hideturtle()
      turtle.speed(0)
      turtle.width(4)
      turtle.title(num)
      turtle.penup()
      turtle.left(180)
      turtle.forward(250)
      turtle.right(90)
      turtle.forward(30)
      turtle.right(180)
      turtle.pendown()

def readZipCode(strZip):
      noDash = ''
      for i in strZip:
            if i != "-":
                  noDash += i
      return noDash

def checkSum(strZip):
      sum = 0
      for i in strZip:
            sum += int(i)
      check = 10 - (sum % 10)
      result = strZip + str(check)
      return result
def transformBarcode(zipCode): 
      removeDash = readZipCode(zipCode)
      final = checkSum(removeDash)
      encoding = "1"
      for i in final:
            if i == "0":
                  encoding += "11000"
            elif i == "1":
                  encoding += "00011"
            elif i == "2":
                  encoding += "00101"
            elif i == "3":
                  encoding += "00110"
            elif i == "4":
                  encoding += "01001"
            elif i == "5":
                  encoding += "01010"
            elif i == "6":
                  encoding += "01100"
            elif i == "7":
                  encoding += "10001"
            elif i == "8":
                  encoding += "10010"
            elif i == "9":
                  encoding += "10100"
      encoding += "1"
      printBarcode(encoding, zipCode)

def printOne():
      turtle.forward(30)
      turtle.left(90)
      turtle.penup()
      turtle.forward(10)
      turtle.left(90)
      turtle.forward(30)
      turtle.left(180)
      turtle.pendown()

def printZero():
      turtle.penup()
      turtle.forward(15)
      turtle.pendown()
      turtle.forward(15)
      turtle.left(90)
      turtle.penup()
      turtle.forward(10)
      turtle.left(90)
      turtle.forward(30)
      turtle.left(180)
      turtle.pendown()

def printBarcode(turtleGuide, zipCode):
      title = "Zip Code: " + zipCode
      draw(title)
      for i in turtleGuide:
        if i == "0":
            printZero()
        else:
              printOne()
      turtle.done()
        
def main():
    zip = input("Enter Zip Code: ")
    transformBarcode(zip)
    turtle.done()

if __name__ == '__main__':
        main()