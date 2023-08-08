class Solution:
    def countDigits(self, num: int) -> int:
        digits = 0
        num_ = num
        while num_ > 0:
            right = num_ % 10
            if not (num % right):  # divisible
                digits += 1
            num_ //= 10
        return digits


if __name__ == "__main__":
    s = Solution()
    print(s.countDigits(1012))
