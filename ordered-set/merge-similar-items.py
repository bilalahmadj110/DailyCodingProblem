from collections import defaultdict
from typing import List, Dict


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        hashmap: Dict[int, int] = defaultdict(int)
        for item1 in items1:
            hashmap[item1[0]] += item1[1]
        for item2 in items2:
            hashmap[item2[0]] += item2[1]
        return self.hashmap_to_sorted_2d_array(hashmap)

    def hashmap_to_sorted_2d_array(self, hashmap: Dict[int, int]) -> List[List[int]]:
        items = list(hashmap.items())
        sorted_items = sorted(items, key=lambda x: x[0])
        sorted_2d_array = [list(item) for item in sorted_items]
        return sorted_2d_array


if __name__ == "__main__":
    s = Solution()
    items1 = [[10, 5], [4, 7], [3, 9]]
    items2 = [[2, 10], [1, 3], [3, 2]]
    print(s.mergeSimilarItems(items1, items2))
