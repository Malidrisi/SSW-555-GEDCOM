import unittest
import datetime

class TestCase (unittest.TestCase): 
    def test_age(self):
        Date = "1992-04-08"
        Today = str(datetime.datetime.now())
        Age = 24
        self.assertTrue(24,Age) 
        self.assertFalse(Today < Date,Age) 

if __name__ == '__main__':
    unittest.main()