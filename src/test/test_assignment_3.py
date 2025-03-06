import unittest
import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from src.main.assignment_3 import (  
  Eulers_Method,
  Runge_Kutta,
)

class TestAssignment2(unittest.TestCase):
  def test_Eulers_Method(self):
    range_end = 2
    range_start = 0
    iterations = 10
    initial_point_y = 1
    f = lambda t, y: t - y**2
    h = (range_end - range_start) / iterations
    print(Eulers_Method(range_start, range_end, iterations, initial_point_y, f, h)[iterations])

  def test_Runge_Kutta(self):
    range_end = 2
    range_start = 0
    iterations = 10
    initial_point_y = 1
    f = lambda t, y: t - y**2
    h = (range_end - range_start) / iterations
    print()
    print(Runge_Kutta(range_start, range_end, iterations, initial_point_y, f, h)[iterations])
    
class NoDotsTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        pass 

class NoDotsTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return NoDotsTestResult(self.stream, self.descriptions, self.verbosity)

if __name__ == "__main__":
    unittest.main(testRunner=NoDotsTestRunner(), verbosity=0)
