class person:
    def __init__(self,name = " ", ID=-1, birthdate="1/1/2000"):
        self.name = name
        self.ID = ID
        self.birthdate = birthdate

    def eat(self):
        print("mmm, dinner")

    def sleep(self):
        print("snore")

    def introduce(self):
        print("hello, my name is " + self.name)