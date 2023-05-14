import collections
from typing import List, Tuple

from day2.heaps import Heaps


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        # O(2N)
        # 1N -> Counter
        # 1N -> list
        num_freq: List[Tuple[int, int]] = list(counter.items())

        heaps = Heaps()
        for tup in num_freq:
            heaps.insert(tup)

        output: List[int] = []
        while k:
            output.append(heaps.pop()[0])
            k -= 1

        return output


if __name__ == "__main__":
    print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
    print(Solution().topKFrequent([1], 1))
