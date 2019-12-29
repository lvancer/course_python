# 装饰器


def deco(f):
    def wrapper():
        print('deco')
        return f()
    return wrapper


# def func():
#     print('func')
#
# deco(func)()

@deco
def func():
    print('func')

func()





from functools import wraps

def deco_name(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        # ...前置操作...
        ret = f(*args, **kwargs)
        # ...后置操作...
        return ret
    return wrapper


def deco_name_args(a, b):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            # ...前置操作...
            ret = f(*args, **kwargs)
            # ...后置操作...
            return ret
        return wrapper
    return decorator

@deco_name_args(1, 2)
def ff():
    pass


import logging, time
def log(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        logging.info('{} call {}'.format(time.time(), f.__name__))
        return func(*args, **kwargs)
    return wrapper


def auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth = kwargs['auth']       # 获取验证信息
        if not auth:                # 验证失败
            return                  # 失败处理
        return f(*args, **kwargs)
    return wrapper