from typing import List

# https://leetcode.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp_num = x
        if x < 0:
            return False
        reverse_num = 0
        while x != 0:
            ones_digit = x % 10
            reverse_num = (reverse_num * 10) + ones_digit
            x = x // 10
        return temp_num == reverse_num


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(121))
