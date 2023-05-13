from collections import defaultdict


def longest_portion(apple_types: list[int]) -> int:
    counter: dict[int, int] = defaultdict(int)
    types_so_far: int = 0

    max_portion: int = 0

    left_pointer: int = 0

    for right_pointer, apple_type in enumerate(apple_types):
        # Increase the variable that keeps track of the total number of detected types thus far.
        if counter[apple_type] == 0:
            types_so_far += 1
        counter[apple_type] += 1

        if types_so_far == 2:
            max_portion = max(max_portion, right_pointer - left_pointer + 1)
        elif types_so_far > 2:
            # [2, 1, 2, 3, 3, 1, 3, 5]
            left_most: int = apple_types[left_pointer]
            while counter[left_most] != 0:
                counter[apple_types[left_pointer]] -= 1
                if counter[apple_types[left_pointer]] == 0:
                    types_so_far -= 1
                left_pointer += 1

    return max_portion


if __name__ == '__main__':
    print(longest_portion([2, 1, 2, 3, 3, 1, 3, 5]))
