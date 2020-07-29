#TDD, red green refactor
# Red is the starting point, write a test > test fails > green stage, code passes > refactor stage, improve code

import unittest
class TestProduct(unittest.TestCase):
    def test_multiplies_two_numbers_together(self):
        self.assertEqual(
            product(3, 5), 
            15
        )

if __name__ == "__main__":
    unittest.main()