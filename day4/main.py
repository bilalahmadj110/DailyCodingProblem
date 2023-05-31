from typing import List


# There are three different methods to solve this question.
def maxVowels(s: str, k: int) -> int:

    left = 0
    a = {'a', 'e', 'i', 'o', 'u'}
    max_vow = 0
    vow_so_far = 0

    for right, ss in enumerate(s):
        ln = right - left + 1

        if ss in a:
            vow_so_far += 1
            max_vow = max(vow_so_far, max_vow)

        if ln >= k:
            l = s[left]
            if l in a:
                vow_so_far -= 1
            left += 1

    return max_vow





if __name__ == "__main__":
    maxVowels("leetcode", 3)
