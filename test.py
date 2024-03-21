
import main
import unittest

class TestMain(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(main.addition(1, 2), 3, "should be 3")
        self.assertEqual(main.addition(5, 5), 10, "should be 10")
        self.assertEqual(main.addition(40, 20), 60, "should be 60")
        self.assertEqual(main.addition(-3, 2), -1, "should be -1")

if __name__ -- '_main_':
    unittest.main()
        