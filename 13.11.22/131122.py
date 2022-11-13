# my_list = [1,2,3,4,5]
# iterator = iter(my_list)
# print(iterator)
# print(*iterator)

# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#
#     def __iter__(self):
#         self.i = 0
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
#
# count = Counter(10)
# print(*count)
# for i in count:
#     print(i)
#     for i in range(10)
#         print(i, end=' ')


# def raise_to_the_degrees(number, max_degrees):
#     i = 0
#     while True:
#         result = number ** i
#         yield number ** i
#         if result > 10000000:
#             return
#         i += 1
#
#
# res = raise_to_the_degrees(10, 5)
# print(res)
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# for _ in res:
#     print(_)

# p = print
# p('Hello')
#
# def external():
#     a = 1
#
#     def inner():
#         print('A =', a)
#     return inner()
#
# a1 = external
# a1()


# def counter():
#     count = 0
#
#     def inner():
#         nonlocal count
#         count +=1
#         return count
#     return inner
# a1 = counter()
# print(a1())
# print(a1())
# print(a1())
# b1 = counter()
# print(b1())
import string
def gen_password():
    pas = ''

    def inner():
        nonlocal pas
        pas += (string.ascii_letters)
        return pas
    return inner

password1 = gen_password()





