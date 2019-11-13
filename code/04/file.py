# 文件

# f = open('a.txt', 'r')  # 打开文件
# content = f.read()      # 读取整个文件
# print(content)

# f = open('a.txt')
# lines = f.readlines()   # 读取所有行
# print(lines)

# 逐行读取
try:
    f = open('a.txt')
    for line in f:
        line = line.strip()
        print(line)
    f.close()
except Exception as e:
    print('文件读取错误')
    exit()


# 写文件
f = open('b.txt', 'w')
f.write('aa\nbb\ncc')
f.close()

# 追加文件
f = open('b.txt', 'a')
f.write('\ndd\nee')
f.close()


# 不重复的单词
import re   # 导入re模块
f = open('license.txt')
words = []
for line in f:
    line = line.strip()             # 去空格回车
    _words = line.lower().split(' ')    # 分割
    for w in _words:
        if not w.isalpha():                 # 包含非字母
            w = re.sub('[^a-zA-Z]', '', w)  # 去除非字母
        if len(w.strip()) != 0:             # 保证不是空内容
            words.append(w)
words = set(words)  # 去重
print(len(words))