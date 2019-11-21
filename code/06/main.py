# 类

# from user import Person
# p1 = Person.Person()
#
# from user.Person import Person
# p1 = Person()


from user import Person

# p1 = Person('Green', 12)
# print(p1.name, p1.age)
p2 = Person('Lucy', 14)
# print(p2.name, p2.age)
p2.sleep(10)
# print(p1.__name, p1.__age)

from user import Student
student1 = Student('Green', 12)
# print(student1.get_name())
student1.sleep(10)

# from user import Programmer
# p = Programmer('Green', 18)
# print(Programmer.count_by_name('Green'))
# count = Programmer.count_by_name('Green')

# 静态继承问题

# class Gx(Programmer):
#     pass
    # programmers = {}  # 静态变量

    # @classmethod
    # def count_by_name(cls, name):
    #     return 123

# p = Programmer('Green', 18)
# print(Gx.count_by_name('Green'))