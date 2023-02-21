# import unittest
from adaptgym.envs.cdmc.suite import cheetah, cartpole

def test_cartpole():
  print(cartpole.balance())
  assert 1 == 1

# class TestCDMC(unittest.TestCase):
#
#   def test_cartpole(self):
#     print(cartpole.balance())
#     self.assertEqual(0, 0)
#
# unittest.main()
