# 列表

name_list = ['Green', 'Lucy', 'Lily']   # 字符串列表
score_list = [98, 67, 80]               # 整数列表
x_list = ['hello', 98, 2.15, True]      # 任意类型列表
y_list = [score_list, name_list]        # 列表的列表

print(len(name_list))   # 列表长度
print(score_list[1])    # 索引，返回元素
print(x_list[0:1])      # 切片，返回列表
print(y_list[1][2])     # 访问多维列表

# 等价于
_name_list = y_list[1]
print(_name_list[2])

# 修改
name_list[2] = 'Kate'

# 逻辑判断
if 'Green' in name_list:
    print('Green is here')
if 'Lucy' not in name_list:
    print('Lucy is not here')

# 加法
x = [1, 3, 2]
y = [4, 6, 5]
z = x + y
print(x + y)

# 乘法
x = [1, 2, 3]
z = x * 3
print(z)

# 最大值与最小值
x = [1, 2, 3]
print(max(x))
print(min(x))

# 排序
x = [1, 2, 4, 5, 3, 2]
x.sort()
print(x)

# 翻转列表
x.reverse()
print(x)

# 索引
x = [1, 2, 3, 2]
i = x.index(2)
print(i)
if 9 in x:
    i = x.index(9)
    print(i)

# 统计元素个数
x = [1, 2, 4, 5, 3, 2]
print(x.count(2))


# 尾部添加
x = [1, 2, 3]
x.append(100)
print(x)
x.extend([200, 300])    # x = x + [200, 300]
print(x)

# 插入元素
x = [1, 2, 3]
x.insert(0, 0)
x.insert(2, 100)
print(x)

# 删除
x = [1, 2, 3, 2]
x.remove(2)     # 删除第一个2元素
# del x[1]        # 删除位置1的元素
# p = x.pop()     # 删除最后一个2，同时p被赋值2
# x.clear()       # 删除所有元素
print(x)







