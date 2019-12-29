# # 匿名方法
# f1 = lambda : 0                     # 无参数
# f2 = lambda x: x if x > 0 else 0    # 单参数
# f3 = lambda x, y: x + y             # 多参数
#
# f3(1, 2)    # 调用
#
# # 函数式编程
# f = lambda x: x*x
# def func(x):
#     return x*x
# print(f)
# print(func)
# x = func    # 赋值
#
# # 参数
# def funcx(f):
#     return f(1)     # 调用传入的方法
# print(funcx(f))     # 将方法作为参数传入

# 过滤
# x = filter(lambda d: d % 2, range(10))
# print(list(x))


# s = sorted([3, 4, 1, 2, -1, -2, -3], key=lambda x: x*x)
# from functools import cmp_to_key
# s2 = sorted([3, 4, 1, 2, -1, -2, -3], key=cmp_to_key(lambda x, y: abs(x) - abs(y)))
# print(s2)

# l = [3, 4, 1, 2, -1, -2, -3]
#
# y = map(lambda x: abs(x), l)    # Map操作
# print(list(y))
#
# from functools import reduce
# z = reduce(lambda a, b: a + b, l)   # Reduce操作
# print(z)


def f():
    def g():        # 方法内定义一个方法
        print('g')
    return g        # 返回一个方法

f()         # 获得方法
f()()       # 调用返回的方法

def lazy_sum(*args):
    def _sum():
        return sum(args)
    return _sum

ret = lazy_sum(1, 2, 3) # 没有马上计算
ret()                   # 调用时计算结果