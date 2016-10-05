import unittest

def unique_individuals(person):
    uniquePerson = {"saloni" : "1993-07-20", "riya" : "1993-07-27"}
    if person.keys() in uniquePerson.keys() and person.values() in uniquePerson.values():
        return False
    else:
        return True 

class TestMyFunctions(unittest.TestCase):          

    def test_unique_individuals(self):
        person = {"saloni" : "1993-07-20"}
        self.assertTrue(True, unique_individuals(person))
        self.assertFalse(False, unique_individuals(person))  
        
if __name__ == "__main__":
    unittest.main(exit=False) 