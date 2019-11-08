# 条件

x = 5
if x > 10:              # if引导条件语句，用冒号结尾
    print('x > 10')     # 当条件语句为True时，执行该语句
    print('end')

# 条件嵌套
x = 5
if x < 10:
    print('x < 10')
    if x > 4:
        print('ok')

if (x < 10) and (x > 4):
    print('ok')

# else
if x < 10:
    print('yes')
else:
    print('default')

# elif
if x == 1:
    print('x == 1')
elif x == 2:
    print('x == 2')
elif x == 3:
    print('x == 3')
else:
    print('out of range')

# 计算器
x = int(input('输入第一个整数：'))
op = input('输入运算符:')
y = int(input('输入第二个整数：'))
answer = 0
if op == '+':
    answer = x + y
elif op == '-':
    answer = x - y
elif op == '*':
    answer = x * y
elif op == '/':
    answer = x / y
else:
    answer = '错误的运算符'
print(answer)