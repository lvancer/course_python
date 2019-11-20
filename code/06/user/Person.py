# 类


# class Person:
#     def __init__(self):
#         pass


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


class Person(object):

    def __init__(self, name, age):
        self.__name = name    # 名字
        self.__age = age      # 年龄

    def sleep(self, t):
        self.__go2bed()
        print('{} sleeps for {} seconds.'
              .format(self.__name, t))

    def __go2bed(self):
        print(self.__name + ' go to bed.')

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

