#class Human:
    #height = 170

#class Student(Human):
    #satiety = 0

#class Worker(Human):
    # satiety = 100
    #pass

#nick = Student()
#anna = Worker()
#print(nick.height)
#print(anna.height)
#print(nick.satiety)
#print(anna.satiety)


#class Grandparent:
    #height = 170
    #satiety = 100
   # age = 70

#class Parent(Grandparent):
    # age = 45

#class Children(Parent):
    #height = 50
    #def __init__(self):
        #print(self.height)
        #print(self.satiety)
       # print(self.age)

  # nick = Children


#class Hello_world:
    #hello = 'hello'
   # _hello = '_hello'
   # __hello = '__hello'
    #def __init__(self):
      #  self.world = 'hello'
       # self._world = '_hello'
        #self.__world = '__hello'
   # def printer(self):
       # print(self.hello)
        #print(self._hello)
       # print(self.__hello)
       # print(self.world)
      #  print(self._world)
       # print(self.__world)

#class Hi(Hello_world):
    #def hi_printer(self):
        # print(self.hello)
       # print(self.world)
       # print(self._hello)
       # print(self._world)
       # print(self.__hello)
       # print(self.__world)
       # print(self._Hello_world__hello)
        #print(self._Hello_world__world)


#hello = Hello_world()
#hello.printer()
#hi = Hi()
#hi.hi_printer()

#class Hello:
    #def __init__(self):
      #  print("Hello")

#class Hello_world(Hello):
   # def __init__(self):
       # super().__init__()
        #print("World")
       # self.name = 'name'
       # super().__init__()

    #def parents(self):
        #print('Children')




#hello_world = Hello_world()
#hello_world.parents()





class Class1:
    var = 20
    def __init__(self):
        self.var = 10

class Class2(Class1):
    def __init__(self):
        print(self.var)
        super().__init__()
        print(self.var)
        print(super().var)

cl = Class2()








