# NameError: name 'List' is not defined for List
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            if map.get(target - nums[i]) is not None:
                first_index = map[target - nums[i]]
                second_index = i
                return [first_index, second_index]
            else:
                map[nums[i]] = i


if __name__ == "__main__":
    nums = [1, 4, 5, 15]
    target = 6
    solution = Solution()
    print(solution.twoSum(nums, target))

# 50:28
