from typing import List, Tuple


class Heaps:

    def __init__(self):
        self.array: List[Tuple[int, int]] = []

    def insert(self, item: Tuple[int, int]) -> None:
        self.array.append(item)
        # trickle up
        self.__trickle_up(len(self.array) - 1)

    def pop(self) -> Tuple[int, int] | None:
        if not len(self.array):
            return None
        top = self.array[0]
        # delete the last element and place it on top to trickle down
        if len(self.array) > 1:
            self.array[0] = self.array.pop()
            self.__trickle_down(0)
        return top

    def __trickle_down(self, index) -> None:
        top = self.array[index]
        while index < int(len(self.array) / 2):
            left_child = Heaps.__left_child(index)
            right_child = left_child + 1
            if right_child < len(self.array) and self.array[left_child][1] < self.array[right_child][1]:
                larger_child = right_child
            else:
                larger_child = left_child
            if top[1] >= self.array[larger_child][1]:
                break
            self.array[index] = self.array[larger_child]
            index = larger_child
        self.array[index] = top

    def __trickle_up(self, index) -> None:
        bottom = self.array[index]
        parent = Heaps.__parent(index)

        while index > 0 and self.array[parent][1] < bottom[1]:
            self.array[index] = self.array[parent]
            index = parent
            parent = Heaps.__parent(parent)
        self.array[index] = bottom

    @staticmethod
    def __parent(x) -> int:
        return int((x - 1) / 2)

    @staticmethod
    def __left_child(x) -> int:
        return int((2 * x) + 1)

    @staticmethod
    def __right_child(x) -> int:
        return int((2 * x) + 2)
