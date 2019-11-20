# 静态

from .Person import Person


class Programmer(Person):

    programmers = {}    # 静态变量

    def __init__(self, name, age):
        Person.__init__(self, name, age)
        if name not in Programmer.programmers:
            Programmer.programmers[name] = 0
        Programmer.programmers[name] += 1

    @classmethod
    def count_by_name(cls, name):
        return cls.programmers[name]

    # @staticmethod
    # def count_by_name(name):
    #     return Programmer.programmers[name]




