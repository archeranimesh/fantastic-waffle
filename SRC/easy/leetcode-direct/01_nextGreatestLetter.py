from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        print(letters, ord(target))
        print(ord("a"))
        print(ord("z"))


if __name__ == "__main__":
    letters = ["c", "f", "j"]
    target = "k"
    solution = Solution()
    print(solution.nextGreatestLetter(letters, target))
