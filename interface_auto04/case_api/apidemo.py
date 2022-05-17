# Author:Shirley
# Date:2022-05-16
import unittest

from ddt import ddt, file_data

from interface_auto04.api_key.interface import Interface


@ddt
class ApiDemo(unittest.TestCase):
    @file_data("../data/login.yaml")
    def test_01(self, **kwargs):
        key = Interface()
        res = key.do_post(url=kwargs['url'], json=kwargs['data'])
        print(res.text)
        self.assertEqual(kwargs['expected'], key.get_text(res.text, 'msg'), msg='pass,预期结果参数错误，实际结果参数错误')


if __name__ == '__main__':
    unittest.main()
