import unittest
from US07 import age_less_than_150

class TestMyFunctions(unittest.TestCase):

    def test_age_less_than_150(self):
        self.assertEqual(age_less_than_150([['I1', 'NAME Maha Idrisi', 'SEX F', 'BIRT Date 1992-04-08', 'DeatDate: Alive', 'FAMC F1'], ['I2', 'NAME Ahmed Idrisi', 'SEX M', 'BIRT Date 1960-01-13', 'DeatDate: Alive', 'FAMS F1', 'FAMC F2']], 0),0)
        self.assertEqual(age_less_than_150([['I1', 'NAME Maha Idrisi', 'SEX F', 'BIRT Date 1800-04-08', 'DeatDate: Alive', 'FAMC F1'], ['I2', 'NAME Ahmed Idrisi', 'SEX M', 'BIRT Date 1960-01-13', 'DeatDate: Alive', 'FAMS F1', 'FAMC F2']],0),1)
        self.assertEqual(age_less_than_150([['I1', 'NAME Maha Idrisi', 'SEX F', 'BIRT Date 1800-04-08', 'DeatDate: Alive', 'FAMC F1'], ['I2', 'NAME Ahmed Idrisi', 'SEX M', 'BIRT Date 1700-01-13', 'DeatDate: Alive', 'FAMS F1', 'FAMC F2']],0),2)

if __name__ == "__main__":
    unittest.main(exit=False)    