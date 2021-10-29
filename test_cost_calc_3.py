import unittest
import numpy as np
from cost_calc import Call

class TestCalcControlFlow(unittest.TestCase):
    def test_cost_1(self):
        self.call = Call(25, 31, 100)
        self.assertEqual(self.call.net_cost, 'Invalid input')

    def test_cost_2(self):
        self.call = Call(15, 31, 100)
        self.assertEqual(self.call.net_cost, 30.94)

    def test_cost_3(self):
        self.call = Call(22, 31, 10)
        self.assertEqual(self.call.net_cost, 1.82)

    
if __name__ == '__main__':
    unittest.main()