# 元组

a = (1, )       # 只有一个元素的元组
b = (1, 3, 4)   # 元组

print(len(a))   # 长度
print(b[1])     # 索引
print(b[0:2])   # 切片
print(max(b))   # 最大值
print(min(b))   # 最小值
print(2 in b)   # in


# 列表与元组转换
tuple([1, 2, 3])    # 转换为元组
list((1, 2, 3))     # 转换为列表

# 拆包
x = ('a', 'b', 'c')
a, b, c = x
print(a, b, c)
