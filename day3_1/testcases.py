import unittest

from day3_1.main import rotate1 as rotate


class MyTestCase(unittest.TestCase):

    def test_longest_portion_example(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        rotate(nums, k)
        print(f"Output for {nums} should be {k} and we get {nums}.")
        self.assertEqual(nums, [5, 6, 7, 1, 2, 3, 4])

    def test_longest_portion_example2(self):
        nums = [-1, -100, 3, 99]
        k = 2
        rotate(nums, k)
        print(f"Output for {nums} should be {k} and we get {nums}.")
        self.assertEqual(nums, [3, 99, -1, -100])


if __name__ == '__main__':
    unittest.main()
