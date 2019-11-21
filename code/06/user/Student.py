from user import Person


class Student(Person):

    def __init__(self, name, age, grade=1):
        Person.__init__(self, name, age)    # 父类构造方法
        self.__grade = grade                # 年级

    def get_grade(self):
        return self.__grade

    def sleep(self, t):
        # print('student ' + self.get_name())
        # Person.sleep(self, t)           # 父类方法
        # print('student {} sleeps for {} seconds.'.format(self.__name, t))
        # print('student {} sleeps for {} seconds.'.format(self.get_name(), t))
        print('student {} sleeps for {} seconds.'.format(self._name, t))

