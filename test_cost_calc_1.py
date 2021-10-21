import unittest
import numpy as np
from cost_calc import Call

class TestCalcBoundaryValue(unittest.TestCase):
    def test_cost_1(self):
        self.call = Call(0, 31, 100)
        self.assertEqual(self.call.gross_cost, 35.0)
        self.assertEqual(self.call.net_cost, 15.47)

    def test_cost_2(self):
        self.call = Call(1, 31, 100)
        self.assertEqual(self.call.gross_cost, 35.0)
        self.assertEqual(self.call.net_cost, 15.47)

    def test_cost_3(self):
        self.call = Call(22, 31, 100)
        self.assertEqual(self.call.gross_cost, 35.0)
        self.assertEqual(self.call.net_cost, 15.47)

    def test_cost_4(self):
        self.call = Call(23, 31, 100)
        self.assertEqual(self.call.gross_cost, 35.0)
        self.assertEqual(self.call.net_cost, 15.47)

    def test_cost_5(self):
        self.call = Call(12, 0, 100)
        self.assertEqual(self.call.gross_cost, 35.0)
        self.assertEqual(self.call.net_cost, 30.94)

    def test_cost_6(self):
        self.call = Call(12, 1, 100)
        self.assertEqual(self.call.gross_cost, 35.0)
        self.assertEqual(self.call.net_cost, 30.94)

    def test_cost_7(self):
        self.call = Call(12, 58, 100)
        self.assertEqual(self.call.gross_cost, 35.0)
        self.assertEqual(self.call.net_cost, 30.94)

    def test_cost_8(self):
        self.call = Call(12, 59, 100)
        self.assertEqual(self.call.gross_cost, 35.0)
        self.assertEqual(self.call.net_cost, 30.94)
                        
    def test_cost_9(self):
        self.call = Call(12, 31, 0)
        self.assertEqual(self.call.gross_cost, 0.0)
        self.assertEqual(self.call.net_cost, 0.0)

    def test_cost_10(self):
        self.call = Call(12, 31, 1)
        self.assertEqual(self.call.gross_cost, 0.35)
        self.assertEqual(self.call.net_cost, 0.36)

    def test_cost_11(self):
        self.call = Call(12, 31, float('inf'))
        self.assertEqual(self.call.gross_cost, float('inf'))
        check = np.isnan(self.call.net_cost)
        self.assertTrue(check)

    def test_cost_12(self):
        self.call = Call(12, 31, 100)
        self.assertEqual(self.call.gross_cost, 35.0)
        self.assertEqual(self.call.net_cost, 30.94)

if __name__ == '__main__':
    unittest.main()