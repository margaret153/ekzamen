class Grandparent:
    def about(self):
        print('I am Grandparent')
    def about_myself(self):
        print('I am Grandparent')
class Parent(Grandparent):
    def about_myself(self):
        print('I am Parent')
class Children(Parent):
    height = 50
    def __init__(self):
        print(self.height)
        print(self.satiety)
        print(self.age)

class Children(Parent):
    def __init__(self):
        super().about()
        super().about_myself()

nick = Children()



class Computer:
    def __init__(self):
        self.resolution = "4K"
class SmartPhone(Computer, Display):
    def printer(self):
        print(self.memory)
        print(self.resolution)

iphone = SmartPhone()
iphone.printer()