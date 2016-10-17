import unittest
from FraudulentActivityNotifications import FraudChecker

class TestStringMethods(unittest.TestCase):

	def atest_median(self):
		elms = [3,4,2,3]
		fraudChecker = FraudChecker([])
		
		self.assertEqual(fraudChecker.select(elms, 0), 2)
		self.assertEqual(fraudChecker.select(elms, 1), 3)
		# self.assertEqual(fraudChecker.select(elms, 2), 3)
		# self.assertEqual(fraudChecker.select(elms, 3), 4)
	
	def test_mediana(self):
		elms = [1,1,1]
		fraudChecker = FraudChecker([])
		self.assertEqual(fraudChecker.select(elms, 1), 1)
		

if __name__ == '__main__':
    unittest.main()