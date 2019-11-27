# 命令行

import os
import sys
# print(sys.argv)     # 获取所有参数


def listdir(path, with_dir=False):
    result = []
    for f in os.listdir(path):
        if with_dir or os.path.isfile(os.path.join(path, f)):
            result.append(f)
    return result


"""
version 1
"""
# if __name__ == '__main__':
#     if sys.argv[1] == '--dir':
#         path = sys.argv[2]
#         with_dir = len(sys.argv) > 3 and sys.argv[3] == 'all'
#         print(listdir(path, with_dir))

"""
version 2
"""

# import argparse
# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()                      # 开启参数解析
#     parser.add_argument('--dir', default='.')               # 必填位置参数
#     parser.add_argument('all', nargs='?', default=False)    # 可选参数，默认为False
#     args = parser.parse_args()
#     print(listdir(args.dir, args.all))


"""
version 3
"""
import argparse
import configparser
if __name__ == '__main__':
    conf = configparser.ConfigParser()
    conf.read('config.ini')
    default_dir = conf.get('INFO', 'dir')   # 获取默认值
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', default=default_dir)
    parser.add_argument('all', nargs='?', default=False)
    args = parser.parse_args()
    print(listdir(args.dir, args.all))

