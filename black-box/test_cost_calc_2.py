import unittest
import numpy as np
from cost_calc import Call

class TestCalcEquivalenceClasses(unittest.TestCase):
    def test_cost_1(self):
        self.call = Call(9, 20, 40)
        self.assertEqual(self.call.gross_cost, 14)
        self.assertEqual(self.call.net_cost, 14.56) 

    def test_cost_2(self):
        self.call = Call(9, 20, 120)
        self.assertEqual(self.call.gross_cost, 42)
        self.assertEqual(self.call.net_cost, 37.13)

    def test_cost_3(self):
        self.call = Call(9, 20, -1)
        self.assertEqual(self.call.gross_cost, 'Invalid input')
        self.assertEqual(self.call.net_cost, 'Invalid input')

    def test_cost_4(self):
        self.call = Call(6, 15, 40)
        self.assertEqual(self.call.gross_cost, 14)
        self.assertEqual(self.call.net_cost, 7.28)

    def test_cost_5(self):
        self.call = Call(6, 15, 120)
        self.assertEqual(self.call.gross_cost, 42)
        self.assertEqual(self.call.net_cost, 18.56)

    def test_cost_6(self):
        self.call = Call(6, 15, -1)
        self.assertEqual(self.call.gross_cost, 'Invalid input')
        self.assertEqual(self.call.net_cost, 'Invalid input')

    def test_cost_7(self):
        self.call = Call(25, 10, 40)
        self.assertEqual(self.call.gross_cost, 'Invalid input')
        self.assertEqual(self.call.net_cost, 'Invalid input')

    def test_cost_8(self):
        self.call = Call(12, 1000, 100)
        self.assertEqual(self.call.gross_cost, 'Invalid input')
        self.assertEqual(self.call.net_cost, 'Invalid input')

    def test_cost_9(self):
        self.call = Call(25, 10, -1)
        self.assertEqual(self.call.gross_cost, 'Invalid input')
        self.assertEqual(self.call.net_cost, 'Invalid input')
    

if __name__ == '__main__':
    unittest.main()
