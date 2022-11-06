# class Human:
#     height = 170
#     satiety = 50
#
#
# class Student(Human):
#     satiety = 0
#
#
# class Worker(Human):
#     # satiety = 100
#     pass
#
#
# nick = Student()
# anna = Worker()
# print(nick.height)
# print(anna.height)
# print(nick.satiety)
# print(anna.satiety)
# class Grandparent:
#     height = 170
#     satiety = 100
#     age = 70
#
#
# class Parent(Grandparent):
#     # age = 45
#     pass
# class Children(Parent):
#     height = 50
#     def __init__(self):
#         print(self.height)
#         print(self.satiety)
#         print(self.age)
#
# nick = Children()

# class Hello_world:
#     hello = 'hello'
#     _hello = '_hello'
#     __hello = '__hello'
#     def __init__(self):
#         self.world = 'hello'
#         self._world = '_hello'
#         self.__world = '__hello'
#     def printer(self):
#         print(self.hello)
#         print(self._hello)
#         print(self.__hello)
#         print(self.world)
#         print(self._world)
#         print(self.__world)
#
# class Hi(Hello_world):
#     def hi_printer(self):
#         print(self.hello)
#         print(self.world)
#         print(self._hello)
#         print(self._world)
#         # print(self.__hello)
#         # print(self.__world)
#         # print(self._Hello_world__hello)
#         # print(self._Hello_world__world)
#
# hello = Hello_world()
# hello.printer()
# hi = Hi()
# hi.hi_printer()

# class Hello:
#     def __init__(self):
#         print("Hello")
#     def parens(self):
#         print('Parens')
#
# class Hello_world(Hello):
#     def __init__(self):
#         # print("World")
#         self.name = 'name'
#         super().__init__()
#
#     def parens(self):
#         print('Children')
#         # super().__init__()
#
#
# hello_world = Hello_world()
# hello_world.parens()


# class Class1:
#     var = 20
#     def __init__(self):
#         self.var = 10
#
# class Class2(Class1):
#     def __init__(self):
#         print(self.var)
#         super().__init__()
#         print(self.var)
#         print(super().var)
#
#
# cl = Class2()

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











