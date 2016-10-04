import unittest
from US29 import ListDeceased

class TestMyFunctions(unittest.TestCase):

    def test_ListDeceased(self):
        self.assertEqual(ListDeceased([['I1', 'NAME Maha Idrisi', 'SEX F', 'BIRT Date 1992-04-08', 'DeatDate: Alive', 'FAMC F1'], ['I2', 'NAME Ahmed Idrisi', 'SEX M', 'BIRT Date 1960-01-13', 'DeatDate: Alive', 'FAMS F1', 'FAMC F2']], 0),"All Indviduals are alive")
        self.assertEqual(ListDeceased([['I1', 'NAME Maha Idrisi', 'SEX F', 'BIRT Date 1992-04-08', 'DeatDate: Alive', 'FAMC F1'], ['I2', 'NAME Ahmed Idrisi', 'SEX M', 'BIRT Date 1960-01-13', 'DEAT Date 1962-08-07', 'FAMS F1', 'FAMC F2']], 0),1)
        self.assertEqual(ListDeceased([['I1', 'NAME Maha Idrisi', 'SEX F', 'BIRT Date 1992-04-08', 'DEAT Date 1962-08-07', 'FAMC F1'], ['I2', 'NAME Ahmed Idrisi', 'SEX M', 'BIRT Date 1960-01-13', 'DEAT Date 1962-08-07', 'FAMS F1', 'FAMC F2']], 0),2)

if __name__ == "__main__":
    unittest.main(exit=False)    