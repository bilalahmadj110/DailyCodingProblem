class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num > 0:
            # num >> n = num/(2^n)
            # num << n = num x 2^n
            # num & 1 returns 1 if num is odd otherwise 0
            # num ^ 1 adds 1 if num is even otherwise subtracts 1
            num = (num ^ 1) if (num & 1) else (num >> 1)
            count += 1
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.numberOfSteps(14))
