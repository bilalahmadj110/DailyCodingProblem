import unittest

from day3.main import remove_duplicates


class MyTestCase(unittest.TestCase):

    def test_longest_portion_example(self):
        apple_trees = [1, 1, 1, 2, 2, 3]
        result = remove_duplicates(apple_trees)
        print(f"Output for {apple_trees} should be 5 and we get %d." % result)
        self.assertEqual(result, 5)

    def test_longest_portion_example2(self):
        apple_trees = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        result = remove_duplicates(apple_trees)
        print(f"Output for {apple_trees} should be 7 and we get %d." % result)
        self.assertEqual(result, 7)

    def test_all_unique(self):
        array = [1, 2, 3, 4]
        result = remove_duplicates(array)
        print(f"Output for {array} should be 4 and we get %d." % result)
        self.assertEqual(result, 4)

    def test_all_unique2(self):
        array = [1, 2]
        result = remove_duplicates(array)
        print(f"Output for {array} should be 2 and we get %d." % result)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
