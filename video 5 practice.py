f = open("newfilename.txt","w")
f.write("hello world!!!!!!\n")
f.write("is this working?\n")
f.write("coding12321\n")
f.close()

f = open("newfilename.txt","r")
lineno = 1
for line in f:
    print(f"{lineno}:{line.strip()}")
    lineno = lineno + 1
f.close()

f = open("madlib.txt","w")
f.write("the quick,\n")
f.write("*adjective\n")
f.write("*noun\n")
f.write("*past-tense verb\n")
f.write("over the lazy\n")
f.write("*noun\n")
f.write(".")
f.close()

f = open("madlib.txt","r")
story = ""
for line in f:
    if line.startswith("*"):
        text = input("give me a(n)" + line[1:].strip() + ":")
    else:
        text = line
    story = story + " " + text.strip()

print("here is your story")
print(story)
f.close()