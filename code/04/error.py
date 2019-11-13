# 异常

# 语法错误
# a = 1
# if a > 2
#     print(1)

# 执行时错误
# a = 10
# b = 0
# print(a / b)

# 异常捕获
try:
    a = 10
    b = 0
    print(a / b)
except Exception as e:
    print(e)

# 异常处理
try:
    a = int(input('输入a：'))
    b = int(input('输入b：'))
    print(a / b)
except ZeroDivisionError:
    print('b不能为0')
except ValueError:
    print('输入的不是数字')
except Exception as e:
    print(e)
finally:
    print('程序结束。')


