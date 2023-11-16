from person import person

class student(person):
    def __init__(self, name=" ", ID=-1, birthdate="1/1/2000"):
        person.__init__(self,name, ID, birthdate)

    def study(self):
        print(student + "is studing")

    def do_homework(self,course):
        print(student + "is doing homework for" + course)

    def ask_question(self):
        print("Wait, what?")

    def introduce(self):
        print("Yo, I'm " + self.name)
