import unittest

class TestMyFunctions(unittest.TestCase):

    def test_birth_before_death(self):
        
        birt_date = "1940-06-11"
        deat_date = "1962-08-07"
        self.assertTrue(True, deat_date > birt_date)
        self.assertFalse(deat_date < birt_date, deat_date > birt_date)  
        
if __name__ == "__main__":
    unittest.main(exit=False)  