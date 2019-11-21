# 类

"""
Version 空类
"""
# class Person:
#     def __init__(self):
#         pass

"""
Version 成员变量与方法
"""
# class Person:
#
#     def __init__(self, name, age):
#         self.name = name    # 名字
#         self.age = age      # 年龄
#
#     def sleep(self, t):
#         self.go2bed()
#         print('{} sleeps for {} seconds.'.format(self.name, t))
#
#     def go2bed(self):
#         print(self.name + ' go to bed.')


"""
Version 访问限制
"""
# class Person(object):
#
#     def __init__(self, name, age):
#         self.__name = name    # 名字
#         self.__age = age      # 年龄
#
#     def sleep(self, t):
#         self.__go2bed()
#         print('{} sleeps for {} seconds.'
#               .format(self.__name, t))
#
#     def __go2bed(self):
#         print(self.__name + ' go to bed.')
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         self.__age = age


"""
Version 继承中的访问限制
"""
class Person(object):

    def __init__(self, name, age):
        self._name = name    # 名字
        self._age = age      # 年龄

    def sleep(self, t):
        self._go2bed()
        print('{} sleeps for {} seconds.'
              .format(self._name, t))

    def _go2bed(self):
        print(self._name + ' go to bed.')

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age




