# https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = ""
        for i in range(len(strs[0])):
            print("i= ", i)
            flag = True
            for j in range(len(strs)):
                print("\tj= ", j)
                if len(strs[j]) > i:
                    if j == 0:
                        cur = strs[0][i]
                        print("\t\tcur: ", cur)
                    else:
                        print("\t\tfirst else:, strs[j][i] ", strs[j][i], " cur: ", cur)
                        if strs[j][i] != cur:
                            flag = False
                            return result
                else:
                    print("2nd else")
                    return result
            if flag:
                result += cur
                print("result: ", result)
        return result  # This return solves the strs3 issue.


if __name__ == "__main__":
    solution = Solution()
    strs = ["abcdefgh", "abcefgh"]
    strs2 = ["flow", "flower", "flight"]
    strs3 = ["flow", "flower", "floww"]
    print(solution.longestCommonPrefix(strs3))
