import unittest

from day1.main import longest_portion


class MyTestCase(unittest.TestCase):

    def test_longest_portion_example(self):
        apple_trees = [2, 1, 2, 3, 3, 1, 3, 5]
        result = longest_portion(apple_trees)
        print("Output for [2, 1, 2, 3, 3, 1, 3, 5] should be 4 and we get %d." % result)
        self.assertEqual(result, 4)

    def test_longest_portion_alternating_types(self):
        apple_trees = [1, 2, 1, 2, 1, 2, 1]
        result = longest_portion(apple_trees)
        print("Output for [1, 2, 1, 2, 1, 2, 1] should be 7 and we get %d." % result)
        self.assertEqual(result, 7)

    def test_longest_portion_single_type(self):
        apple_trees = [3, 3, 3, 3]
        result = longest_portion(apple_trees)
        print("Output for [3, 3, 3, 3] should be 0 and we get %d." % result)
        self.assertEqual(result, 0)

    def test_longest_portion_unique_types(self):
        apple_trees = [4, 5, 6, 7, 8]
        result = longest_portion(apple_trees)
        print("Output for [4, 5, 6, 7, 8] should be 2 and we get %d." % result)
        self.assertEqual(result, 2)

    def test_quora(self):
        apple_trees = [1, 2, 2, 3, 3, 3, 4, 5, 6]
        result = longest_portion(apple_trees)
        print(f"Output for {apple_trees} should be 5 and we get {result}.")
        self.assertEqual(result, 5)

    def test_akashravichandran1(self):
        apple_trees = [2, 1, 2, 2, 2, 1, 2, 1]
        result = longest_portion(apple_trees)
        print(f"Output for {apple_trees} should be 8 and we get {result}.")
        self.assertEqual(result, 8)

    def test_akashravichandran2(self):
        apple_trees = [1, 2, 3, 4]
        result = longest_portion(apple_trees)
        print(f"Output for {apple_trees} should be 2 and we get {result}.")
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
