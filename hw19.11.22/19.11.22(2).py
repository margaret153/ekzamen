
def gener(b):
    for i in b:
        yield i

a = [1, 2, 3, 4, 5, 6, 7]
b = a.__iter__()
print(gener(b).__next__())


