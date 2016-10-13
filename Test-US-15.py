import unittest
from US15 import fewerThan15Siblings

class TestMyFunctions(unittest.TestCase):

    def test_fewer_than_15_siblings(self):
        wr = open('testOutput.txt','w')
        FamList = [['F1', 'HUSB I1', 'WIFE I2', 'CHIL I1', 'CHIL I9', 'CHIL I10', 'MARR Date 1985-01-01', 'DIV Date 1990-04-04']]
        self.assertFalse(fewerThan15Siblings(FamList, wr))

if __name__ == "__main__":
    unittest.main(exit=False)    