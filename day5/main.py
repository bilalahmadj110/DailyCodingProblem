from typing import List


def numSubarraysWithSum(nums: List[int], goal: int) -> int:
    cur_sum, prev_sum = 0, 0

    left = 0
    left_zeros = 0
    right_zeros = 0

    for right, num in enumerate(nums):
        cur_sum += num

        if prev_sum == 0:
            left_zeros = right
        if cur_sum == goal:
            right_zeros += 1

        if cur_sum > goal:
            prev_sum = cur_sum


if __name__ == "__main__":
    numSubarraysWithSum([0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], 2)
