evens = [2*x for x in range(0,100)]
hs = [h for h in evens if h > 100]
print(hs)

songs = ["beat it","eat it","jingle bells"]
word = input("give me a song word ")
choices = [s for s in songs if word in s.split(' ')]

for i,c in enumerate(choices):
    print(f"{i+1}: {c}")

# f = open("class practice 11-8.py", "r")
# contents = f.read()
# idx = 0
# while idx != -1:
#     idx = contents.find("for",idx)
#     print = (contents[idx:idx + 10])
#     if idx != -1:
#        idx = idx + 1

# import random

# items = [random.randint(0,1000) for x in range(0,100)]
# print(items)

import os 

if 'hello.txt' in os.listdir():
    f = open('hello.txt')
    contents = f.readline()
    parts = contents.split(':')
    name = parts[1].strip()
    contents = f.readline()
    