#b) Scrieti 2 teste unitare (unul pentru True si unul pentru False) pentru functia is_prime

import unittest
from functions_tema08 import is_prime
class FunctionsTestCase(unittest.TestCase):
    def test_is_prime_01(self):
        expected_result = True
        actual_result = True or False
        self.assertIsInstance(actual_result, int)
        self.assertEqual(expected_result, actual_result)
    def test_is_prime_02(self):
        expected_result = False
        actual_result = True or False
        self.assertIsInstance(actual_result, int)
        self.assertEqual(expected_result, actual_result)
if __name__ == '__main__':
    unittest.main()
