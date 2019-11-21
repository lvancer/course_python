# 单元测试

import unittest         # 单元测试框架
from user import Student    # 要测试的类


class TestStudentMethods(unittest.TestCase):

    def test_student(self):         # 测试用例
        s = Student('Green', 12)
        self.assertEqual(12, s.get_age())
        self.assertEqual('Green', s.get_name())


if __name__ == '__main__':  # 当作为启动文件时
    unittest.main()