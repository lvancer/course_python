# 循环

names = ['Green', 'Lucy', 'Lily']
for name in names:
    print('Happy Birthday, {}'.format(name))


# 计算总和
numbers = [10, 53, 45, 44, 907] # 要计算的列表
answer = 0                      # 总和初始化为0
for i in numbers:               # 开始循环
    answer = answer + i         # 逐个相加
print(answer)
print(sum(numbers))             # sum方法

# 结束循环
numbers = [10, 53, 45, 44, 907]
i = 0                   # 记录当前遍历到的位置
index = -1              # 结果默认为-1不存在
for number in numbers:
    if number == 53:    # 满足条件
        index = i       # 赋值位置
        break           # 停止循环
    i = i + 1           # 位置+1
print(index)

# 中断循环
numbers = [10, 53, 45, 44, 907]
answer = 0
for i in numbers:
    if i > 100:
        continue    # 马上开始下一个循环
    answer = answer + i
print(answer)

# if i <= 100:
#     answer = answer + i

# while循环
names = ['Green', 'Lucy', 'Lily']
i = 0   # 索引位置从0开始
while i < len(names):   # 条件为True时c，继续循环
    name = names[i]     # 通过索引获得元素
    print('Happy Birthday, {}'.format(name))
    i = i + 1   # 索引+1

# 无限循环
# while True:
#     print(1)

# range
for i in range(10):     # 0到9的序列
    print(i)
range(3, 10)    # 3到9的序列
range(3, 10, 2) # 3,5,7,9 步长为2的序列

names = ['Green', 'Lucy', 'Lily']
for i in range(len(names)):
    name = names[i]
    print('Happy Birthday, {}'.format(name))

# 循环的嵌套
for i in range(1, 10):
    for j in range(1, 10):
        print('{} * {} = {}'.format(i, j, i*j))

for i in range(1, 10):
    for j in range(1, 10):
        if j < i:
            continue
        print('{} * {} = {}'.format(i, j, i*j))

# 字典的循环
user = {'name': 'Green', 'age': 12, 'address': 'china'}
for key in user.keys():
    print('{} : {}'.format(key, user[key]))

for key, value in user.items():
    print('{} : {}'.format(key, value))
