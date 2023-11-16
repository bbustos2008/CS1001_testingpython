from person import person
from student import student
from teacher import teacher

def main():
    t = teacher(name="smith")
    s = student(name="jones")
    people = [teacher(name="anderson"), teacher(name = "su"),student("ramirez")]

    s.sleep()
    t.eat()

    for p in people:
        p.introduce()
        p.sleep()
        p.eat()

        if type(p) is teacher:
            p.teach()
        elif type is student:
            p.do_homework()

if __name__ == "__main__":
    main()