# 布尔值

# 数字
a = 5
b = a == 5  # True
b = a != 5  # False
b = a > 2   # True
b = a < 4   # False

# 字符串
s = 'abc'
b = s == 'abc'  # True
b = s.find('a') > 0     # 判断是否存在a，True
b = s.find('e') > 0     # 判断是否存在e，False
b = s.startswith('b')   # 判断是否以b开头，False
b = s.endswith('c')     # 判断是否以c结尾，True

# 运算
a = True
b = False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False

print(a or b and (a or b) and not b)
