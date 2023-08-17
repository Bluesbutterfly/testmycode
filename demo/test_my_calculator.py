import unittest
from my_calculator import add_number,Sentence
class TestmyAdder(unittest.TestCase):
  def setUp(self):
    self.sentence = Sentence("hello")
  def test_positive_with_positive(self):
    self.assertEqual(add_number(5,3),8)
  def test_negative_with_positive(self):
    self.assertEqual(add_number(-5,3),-2)
