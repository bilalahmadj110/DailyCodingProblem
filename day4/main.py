from typing import List


def remove_duplicates(nums: List[int]) -> int:
    if len(nums) < 2:
        return len(nums)

    cur_count, track_count = 0, 0
    last_num = None

    for i, num in enumerate(nums):
        if num == last_num:
            cur_count += 1
        else:
            cur_count = 1
            last_num = num

        if cur_count < 3:
            nums[track_count] = num
            track_count += 1
    return track_count


if __name__ == "__main__":
    remove_duplicates([1, 2, 3, 4, 5, 6, 7])
