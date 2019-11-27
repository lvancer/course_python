# 系统模块

import os
import sys


"""
系统常量
"""

# # 当前系统
# print(sys.platform)
#
# # Python环境
# print(sys.version.split()[0])   # 获得Python版本
# print(sys.executable)           # 获得Python的执行文件
# print(sys.path)                 # 获得Python代码的所有目录
#
# # 跨平台的符号
# print(os.linesep)       # 换行符，Unix为 \n ，Win32为 \r\n
# print(os.sep)           # 文件路径分隔符，Unix为 /，Win32为 \
# print(os.pathsep)       # 多个文件路径间的分隔符，Unix为 :，Win32为 ;
#
# # 其他不重要的
# print(sys.maxsize)      # 整数最大值 9223372036854775807
# print(sys.winver)       # 主版本号 3.6
# print(os.curdir)        # 当前目录 .
# print(os.pardir)        # 上一级目录 ..
# print(sys.copyright)    # 版权信息

"""
文件
"""

# 几个常量
# print(os.path.sep)      # 路径分隔符 (Unix为 /，Win为 \\)
# print(os.path.pathsep)  # 多个路径间的分隔符，多用于环境变量 (Unix为 :， Win为 ;)
# print(os.path.extsep)   # 后缀名符号 一般为 .

# 路径组合
# path = os.path.join('newdir', 'python.txt')
# print(path)

# 路径分割
# _dir, _file = os.path.split(path)   # 分割成目录和文件
# print(_dir)                     # 目录
# print(_file)                    # 文件
# print(os.path.dirname(path))    # 与_dir一样
# print(os.path.basename(path))    # 与_file一样
# _filename, _ext = os.path.splitext(_file)   # 文件名和扩展名
# print(_filename, _ext)

# 路径变换
# print(os.path.relpath(path))    # 获得相对于当前路径的路径
# print(os.path.abspath(path))    # 绝对路径
# f1 = 'newdir/py/file.txt'
# f2 = 'newdir/py/l1/file.txt'
# f3 = 'newdir/py/l2/file.txt'
# print(os.path.commonprefix([f1, f2, f3])) # 获得多个路径中的共同路径

# 判断路径存在
# print(os.path.exists(path))      # 判断是否存在
# print(os.path.isdir(path))       # 判断是否文件夹
# print(os.path.isfile(path))      # 判断是否文件

# 文件属性
# print(os.path.getatime('./os1.py'))     # 访问时间
# print(os.path.getmtime('./os1.py'))     # 修改时间
# print(os.path.getctime('./os1.py'))     # 创建时间
# print(os.path.getsize('./os1.py'))      # 文件大小

# 创建目录
# os.mkdir('./newdir')     # 创建目录
# os.mkdir('./newdir2/abc')       # 错误，newdir2文件夹并不存在
# os.makedirs('./newdir2/abc')    # 正确，创建多级目录

# 删除目录
# os.rmdir('./newdir')            # 删除目录
# os.removedirs('./newdir2/abc')  # 删除多级目录

# 删除文件
# open('./abc.txt', 'w').close()  # 创建一个文件
# os.remove('./abc.txt')  # 删除文件

# 文件移动
# os.rename('./abc.txt', './ccc.txt')

# 文件列表
# print(os.listdir('../'))
#
# import glob
# print(glob.glob('../*/*.py'))
#
# # 遍历文件夹
# for root, dirs, files in os.walk('../06/'):
#     for f in files:
#         filename = os.path.join(root, f)
#         print(filename)




