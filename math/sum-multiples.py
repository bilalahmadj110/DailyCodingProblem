class Solution:
    def sum_of_multiples(self, n: int) -> int:
        total_sum = 0
        for i in range(1, n + 1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                total_sum += i
        return total_sum


if __name__ == "__main__":
    s = Solution()
    print(s.sum_of_multiples(10))
