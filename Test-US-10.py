import unittest
from US10 import marriageAfter14

class TestMyFunctions(unittest.TestCase):

    def test_marriage_after_14(self):
        wr = open('testOutput.txt','w')
        IndList = [['I1', 'NAME Maha Idrisi', 'SEX F', 'BIRT Date 1992-04-08' ,'DeatDate: Alive', 'FAMC F1'],['I2', 'NAME Saloni Setia', 'SEX F', 'BIRT Date 1800-04-08', 'DeatDate: Alive', 'FAMC F1']]
        FamList = [['F1', 'HUSB I1', 'WIFE I2', 'CHIL I1', 'CHIL I9', 'CHIL I10', 'MARR Date 1985-01-01', 'DIV Date 1990-04-04']]
        self.assertTrue(marriageAfter14(IndList, FamList, wr))

if __name__ == "__main__":
    unittest.main(exit=False)    