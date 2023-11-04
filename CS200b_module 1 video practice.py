import random

def sequentialsearch(haystack,needle):
    for i in range(0,len(haystack)):
        if (haystack[i]== needle):
            return i
    return -1

def main():
    numbers = []
    for i in range(0,1000):
        numbers.append(random.randrange(0,2000))

    target = random.randrange(0,2000)
    location = sequentialsearch(numbers,target)
    if location == -1:
        print("couldn't find " + str(target))
    else:
        print("found " + str(target) + "at" + str(location))

main()

def randomstrings():
    letters = "abcdefghijklmnopqrstuvwxyz"
    strings = []
    for i in range (0,1000):
        length = random.randrange(5,15)
        s = ""
        for c in range(0,length):
            i = random.randrange(0,len(letters))
            s = s + letters[i] 
        strings.append(s)
    return strings

def stringsearch():
    strings = []
    for i in range (0,1000):
        strings.append(random.randrange(5,15))
    
    target = random.randrange(5,15)
    location = randomstrings(strings,target)
    if location == -1:
        print("could't find " + target)
    else:
        print("found " + str(target) + "at " + str(location))

stringsearch()