import unittest
from US05 import marrBeforeDeath

class TestMyFunctions(unittest.TestCase):

    def test_marr_before_death(self):
        wr = open('testOutput.txt','w')
        IndList = [['I1', 'NAME Maha Idrisi', 'SEX M', 'BIRT Date 1992-04-08' ,'DeatDate: Alive', 'FAMC F1'],['I2', 'NAME Saloni Setia', 'SEX F', 'BIRT Date 1800-04-08', 'DeatDate: 1984-01-01', 'FAMC F1']]
        FamList = [['F1', 'HUSB I1', 'WIFE I2', 'CHIL I1', 'CHIL I9', 'CHIL I10', 'MARR Date 1985-01-01', 'DIV Date 1990-04-04']]
        self.assertTrue(marrBeforeDeath(IndList, FamList, wr))

if __name__ == "__main__":
    unittest.main(exit=False)    
