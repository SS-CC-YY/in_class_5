import unittest
import leap_year


class TestCase(unittest.TestCase):
    def test_input_1(self):
        self.assertEqual(leap_year.check_user_input(2020), 2020)
    
    def test_check_1(self):
        self.assertEqual(leap_year.check_leap_year(2020), 0)
    
    def test_check_2(self):
        self.assertEqual(leap_year.check_leap_year(2021), -1)

if __name__ == "__main__":
    unittest.main(verbosity=2)