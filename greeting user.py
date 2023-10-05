username = input("what is your name?")
print(f"welcome {username}")

#madlibs
adjective = input("pick an adjective: ")
noun  = input("pick a noun: ")
verb = input("pick a past-tense verb: ")
print(f"the {noun} {verb} the {adjective} cat")

#bearsvscheeseheads
bears = int(input("How many points did the Bears score?"))
packers = int(input("How many points did the packers score?"))
if bears > packers:
  print("Bear down!")
else:
  print("BOO!!")

#userage

age = int(input("how old are you?"))
if age < 0:
  print("invalid age")
if age >= 16:
  print("you can drive")
if age >= 18:
  print("you can vote")
if age >= 21:
  print("you can enjoy a beer")

  #rock,paper,scissors
import random

comp = random.randint(1,3)
user = int(input("pick 1 for rock, 2 for paper, or 3 for scissors "))
if user != 1 and user != 2 and user != 3:
  print("invalid input. You lose!")
else:
   if comp == user:
     print("tie")
   elif (comp == 1 and user == 3) or (comp ==2 and user ==1) or (comp == 3 and user == 2):
     print("the computer won")
   else:
     print("you won")