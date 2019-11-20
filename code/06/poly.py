# 多态

from user import Student
from user import Person

p1 = Person('Green', 12)
s1 = Student('Green', 12)
print(type(s1))
print(type(p1))

print(isinstance(p1, Person))
print(isinstance(p1, Student))

print(type(p1) == Person)
print(type(p1) == Student)

type(s1) == Person          # False
type(s1) == Student         # True
isinstance(s1, Person)      # True
isinstance(s1, Student)     # True


def poly_test(person):
    if not isinstance(person, Person):
        raise ValueError('数据类型传入错误')
    return person.sleep(10)


try:
    poly_test(p1)
    poly_test(s1)
except ValueError as e:
    print(e)

