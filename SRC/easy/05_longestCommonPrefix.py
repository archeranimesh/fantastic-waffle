# https://leetcode.com/problems/longest-common-prefix/
from typing import List

# 1:36:36


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        short_str = min(strs, key=len)
        print("short_str: ", short_str)

        for i, char in enumerate(short_str):
            print("i: ", i, " char: ", char)
            for other in strs:
                if other[i] != char:
                    return short_str[:i]
        return short_str


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(["abcdefgh", "abcefgh"]))
