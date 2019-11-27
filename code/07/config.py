# 配置

import configparser

# 读取
conf = configparser.ConfigParser()  # 创建对象
conf.read('config.ini')             # 读取文件
# print(conf['DEFAULT']['dir'])       # 获取配置
# print(int(conf['INFO']['x']))
# print(conf['INFO']['save'] == 'True')

# conf.get('DEFAULT', 'dir')       # 获取配置
# conf.getint('INFO', 'x')         # int
# conf.getboolean('INFO', 'save')  # boolean

# 判断
# conf.has_section('DEFAULT')     # 是否存在section
# conf.has_option('INFO', 'dir')  # 是否存在option

# 配置遍历
# print(conf.sections())          # 返回所有section
# print(conf.options('INFO'))     # 返回section下所有options
# for group, section in conf.items():
#     for key, value in section.items():
#         print('conf[{}][{}] = {}'.format(group, key, value))


# 配置修改
conf.add_section('DEBUG')                   # 添加新section
conf.set('DEBUG', 'y', '1')                 # 添加新option
conf.set('INFO', 'dir', 'C:/Users/lin02')   # 修改option
with open('config.ini', 'w') as f:
    conf.write(f)                           # 写入文件

