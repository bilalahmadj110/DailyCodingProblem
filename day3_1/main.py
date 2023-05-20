from typing import List


# There are three different methods to solve this question.

def rotate1(nums: List[int], k: int) -> None:
    k = k % len(nums)

    shifted = len(nums) - k - 1
    pos = len(nums) - 1
    ks = nums[shifted + 1:]

    while shifted >= 0:
        nums[pos] = nums[shifted]
        pos -= 1
        shifted -= 1

    while pos >= 0:
        nums[pos] = ks.pop()
        pos -= 1


def reverse(nums: List[int], start: int, end: int):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


def rotate2(nums: List[int], k: int) -> None:
    k = k % len(nums)
    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)


if __name__ == "__main__":
    rotate2([1, 2, 3, 4, 5, 6, 7], 3)
