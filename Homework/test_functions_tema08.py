#b) Scrieti 2 teste unitare (unul pentru True si unul pentru False) pentru functia is_prime

import unittest
from functions_tema08 import is_prime,list_of_primes_in_interval
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

    def test_list_of_primes_in_interval_01(self):
        test_int = (9,1)
        expected_result = [1,2,3,5,7,]

        actual_result = prime_numbers(9,1)
        self.assertIsInstance(actual_result, list)
        self.assertEqual(actual_result, expected_result)

    def test_list_of_primes_in_interval_02(self):
        test_int = (11, 1)
        expected_result = [1, 2, 3, 5, 7,11 ]

        actual_result = prime_numbers(11, 1)
        self.assertIsInstance(actual_result, list)
        self.assertEqual(actual_result, expected_result)

if __name__ == '__main__':
    unittest.main()