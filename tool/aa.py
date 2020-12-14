import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        print("吃饭")
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
