from person import person

class teacher(person):
    def __init__(self, name=" ", ID=-1, birthdate="1/1/2000"):
        person.__init__(self,name, ID, birthdate)

    def teach(self):
        print(self.name + "is teaching")

    def assign_homework(self, course):
        print(self.name + "assigned homework for their" + course + "course")

    def answer_question(self):
        print(self.name + "is answering student questions")

    def introduce(self):
        print("Hello, I am proffessor " + self.name)