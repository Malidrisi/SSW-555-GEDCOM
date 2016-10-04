import unittest
import datetime
class TestCase (unittest.TestCase): 
    def test_date(self):
        Date = "1992-04-08"
        Today = str(datetime.datetime.now())
        result = Today > Date
        self.assertTrue(True,result) 
        self.assertFalse(Today < Date,result) 

if __name__ == '__main__':
    unittest.main()