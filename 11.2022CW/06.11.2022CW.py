class Human:
    height = 170

class Student(Human):
    satiety = 0

class Worker(Human):
    # satiety = 100
    pass

nick = Student()
anna = Worker()
print(nick.height)
print(anna.height)
print(nick.satiety)
print(anna.satiety)


class Grandparent:
    height = 170
    satiety = 100
    age = 70

class Parent(Grandparent):
    age = 45

class Children(Parent):
    height = 50
    def __init__(self):
        print(self.height)
        print(self.satiety)
        print(self.age)

nick = Children


