# 迭代器

# l = [1, 2, 3, 4, 5]
# it = iter(l)        # 创建迭代器
# i = next(it)        # 获取下一个
# while True:            # next的循环输出
#     print(i)
#     try:
#         i = next(it)
#     except StopIteration:
#         break
#
# # 迭代器类型用于for循环
# for i in it:
#     print(i)


# class PowerIter:
#
#     def __init__(self, power, max=1000):
#         self.data = 0
#         self.power = power
#         self.max = max
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.data += 1
#         ret = self.data ** self.power
#         if ret > self.max:
#             raise StopIteration
#         return ret
#
# iter = PowerIter(2)
# print(next(iter))
# print(next(iter))
#
# for i in iter:
#     print(i)


def power_iter(power, max=1000):
    data = 0
    while True:
        data += 1
        ret = data ** power
        if ret > max:
            return
        yield ret       # 生成器

x = power_iter(2)
# print(next(x))
# print(next(x))

print(list(x))


[i ** 2 for i in range(100)]





