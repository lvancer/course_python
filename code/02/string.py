# 转换与拼接
age = str(12)
name = 'Green'
s = name + ' is a ' + age + ' years old'
print(s)

# 格式化输出
name = 'Green'
s = '{} is a {} years old'.format(name, 12)
print(s)

# name = input('输入名字：')
# age = input('输入年龄：')
# print('{} is a {} years old'.format(name, age))

# 长度
s = 'abcdefg'
l = len(s)
print('length is ' + str(l))

# 截取
s = 'abcdefg'
print(s[1])     # 取某一位
print(s[3:5])   # 取某一段，3到5但不包含5
print(s[2:])    # 从第2位取到最后
print(s[:4])    # 从第1位取到第4位


# 大小写
word = 'i love you'
print(word.upper())        # 大写
print(word.lower())        # 小写
print(word.capitalize())   # 首字母大写
# 去空格
print(' abc '.strip())     # 去空格
# 查找与替换
print('I love you'.find('you'))     # 找到返回位置
print('I love you'.find('me'))      # 未找到返回-1
print('I love you'.replace('you', 'me'))    # 将you替换成me



