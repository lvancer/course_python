# 不定参数

def func(*args):        # 不定参数
    print(len(args))    # 不定参数个数
    print(args)         # 参数是一个元组
    print(args[0])      # 参数获取


func('arg1', 'arg2', 4) # 可以写入任意多个参数

def func2(**kw):        # 字典型不定参数
    print(kw)           # 参数是一个字典
    print(kw['a'])      # 获取参数


func2(a=1, b=2, c=3)    # 可以写入任意多个赋值的参数

# def func3(name, *args)
# def func3(name, **kw)
# def func3(name, *args, **kw)


t = [1, 2, 3, 4, 5, 6]
func(*t)        # 列表拆包为参数

d = {'a': 1, 'b': 2}
func2(**d)      # 字典拆包为参数


# import pymysql
# connect_info = {
#     'host': '127.0.0.1',
#     'port': 3306,
#     'user': 'root',
#     'password': '123456',
#     'db': 'test'
# }
# conn = pymysql.connect(**connect_info)