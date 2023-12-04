import unittest
import char

class TestCalc(unittest.TestCase):

    def test_1(self):
          self.assertEqual(char.char(1), 'doggy')
          self.assertEqual(char.char(0), 'pepe')
          self.assertEqual(char.char(2), 'wojak')

    def test_2(self):
        ch = char.char(1)
        self.assertEqual(ch, 'doggy')
        ch = char.char(0)
        self.assertEqual(ch, 'pepe')
        ch = char.char(2)
        self.assertEqual(ch, 'pepe')

if __name__ == '__main__':
    unittest.main()
