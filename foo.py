import unittest
import os

class Bitemporal(unittest.TestCase):
  def test_foo(self):
    env_var = os.environ.get("MARK_KEY")
    self.assertIsNotNone(env_var, f"no env var {list(os.environ)}")
