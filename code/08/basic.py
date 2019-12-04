# 基本使用

import re

# 定义正则表达式
reg_exp = r'[^a-zA-Z]'  # 匹配非字母

# 匹配一个对象
ret = re.match(reg_exp, '12')
if ret is not None:
    print(ret.group())  # 匹配到一个

ret = re.match(reg_exp, 'a12')
print(ret)      # 空
ret = re.search(reg_exp, 'a12')
print(ret.group())      # 正常返回1

# 查找全部匹配
ret = re.findall(reg_exp, 'a133bbd2')
print(ret)
for i in re.finditer(reg_exp, 'a12'):
    print(i.group(), i.span())

# 替换
ret = re.sub(reg_exp, '*', 'a12')
print(ret)