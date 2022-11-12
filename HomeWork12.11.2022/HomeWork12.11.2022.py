class Tree_Seeds:
    def about(self):
        print('I am Tree Seeds')
    def about_myself(self):
        print('I am Tree Seeds')
class Blackberry_Tree(Tree_Seeds):
    def about_myself(self):
        print('I am Blackberry Tree')
class Berry(Blackberry_Tree):
    height = 3
    def __init__(self):
        print(self.height)
        print(self.satiety)
        print(self.age)

class Blackberry(Berry):
    def __init__(self):
        super().about()
        super().about_myself()



