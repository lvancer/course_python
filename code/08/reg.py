import re

# 前后匹配

re.search(r'^abc', 'abc1')
re.search(r'c1$', 'abc1')

# 字符匹配
re.search(r'.\s.', 'I am a student.')       # I a
re.search(r'\d', 'I am a student.')         # None
re.search(r'stu..nt', 'I am a student.')    # student

re.search(r'[abcde]', 'I am a student.')    # a
re.search(r'[^abcde]', 'I am a student.')   # I
re.search(r'[a-z]', 'I am a student.')      # a

# 重复匹配
print(re.findall(r'\w*', 'You are good'))
print(re.findall(r'\w+', 'You are good'))
print(re.findall(r'\w{1,3}', 'You are good'))

print(re.findall(r'@ab?', '@abc@abc@'))
print(re.findall(r'@.+@', '@abc@abc@'))     # 贪婪
print(re.findall(r'@.+?@', '@abc@abc@'))    # 非贪婪

# 分组
mail = 'lin029011@163.com'
ret = re.match(r'(.+)@(.+)', mail)
print(ret.group())      # 没有变化
print(ret.groups())     # 分组结果

url = 'https://github.com/lvancer/course_python.git'
ret = re.match(r'(\w+)://(.+?)/(.+)\.(\w+)', url)
print(ret.group())
print(ret.groups())