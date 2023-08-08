def is_palindrome(s: str) -> bool:
    if len(s) == 0:
        return True
    return is_palindrome_(s, 0, len(s) - 1)


def is_palindrome_(s: str, left: int, right: int) -> bool:
    if left >= right:
        return True
    if not (s[left].isalpha() or s[left].isnumeric()):
        return is_palindrome_(s, left + 1, right)
    if not (s[right].isalpha() or s[right].isnumeric()):
        return is_palindrome_(s, left, right - 1)
    if s[left].lower() != s[right].lower():
        return False
    return is_palindrome_(s, left + 1, right - 1)


if __name__ == "__main__":
    print(is_palindrome("A man, a plan, a canal: Panama"))
