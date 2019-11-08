# 集合

set1 = {'apple', 'orange', 'melon'}
set2 = {'apple', 'pear'}

# 列表去重
print(set([1, 3, 3, 4]))    # 列表去重
print(set('class'))         # 字符串也是一种序列

# 数学运算
set1 = {'apple', 'orange', 'melon'}
set2 = {'apple', 'pear'}
print(set1 & set2)  # 交集
print(set1 | set2)  # 并集
print(set1 - set2)  # 差集
print(set1 ^ set2)  # 对称差集

# 添加
s = {'apple', 'orange'}
s.add('pear')
print(s)

# 删除
s.remove('apple')       # 如果不存在该元素，会报错。
s.discard('apple1')     # 更安全的删除，即使不存在也不报错
x = s.pop()             # 随机删除集合是中的一个元素，并返回它
s.clear()               # 删除集合中的所有元素
print(s)

# 子集与超集的判断
set1 = {'a', 'b', 'c'}
set2 = {'a'}        # set2是set1的子集，set1是set2的超集
set2.issubset(set1)     # 返回True
set1.issuperset(set2)   # 返回True
