# 方法
def print_with_name(content):
    print(content)
    print('-- Green')

# 方法调用
print_with_name('Hello')

# 多参数
def print_with_name_v2(content, name):
    print(content)
    print('-- {}'.format(name))

print_with_name_v2('Hello', 'Green')

# 默认值
def print_with_name_v3(content, name='Green'):
    print(content)
    print('-- {}'.format(name))
print_with_name_v3('Hello')
print_with_name_v3('Hello', 'Lily')

# def func1(a, b=1, c, d=True):   # 错误
# def func2(a, c, b=1, d=True):   # 正确

# 参数赋值
def func3(a, b, c=1, d=True):
    pass
func3(10, 20, d=False)
func3(b=10, a=20, d=False)


# 返回值
def sum1(numbers):
    answer = 0
    for i in numbers:
        answer = answer + i
    return answer
answer = sum1([10, 53, 45, 44, 907])

# 多返回值
def sum_avg(numbers):
    answer = 0
    for i in numbers:
        answer = answer + i
    return answer, answer/len(numbers)
sum, avg = sum_avg([10, 53, 45, 44, 907])

