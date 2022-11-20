result = []
def divider(a, b):
    if a < b:
        raise ValueError
     if b > 100:
        raise IndexError
    return a/b
data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8 : 4}
for key in data:
    res = divider(key, data[kem])
    result.append(res)

print(result)


# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#
#     def __iter__(self):
#         self.i = -1
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number-1:
#             raise StopIteration
#         return self.i
#
# count = Counter(10)
# # print(*count)
# # for i in count:
# #     print(i)
# for i in Counter(10):
#     print(i, end=' ')
# print()
# for i in range(10):
#     print(i, end=' ')l