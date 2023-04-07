infile = open("input.txt", "r")   #line 1
word = infile.readline()   #line 2
word = word.rstrip()  #line 3
total = sum(word)   #line 4
print(total) 