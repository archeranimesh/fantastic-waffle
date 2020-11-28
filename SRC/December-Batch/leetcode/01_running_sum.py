# https://leetcode.com/problems/running-sum-of-1d-array/
# 1480. Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
from typing import List


class Solution(object):
    """
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
    Return the running sum of nums.
    """

    def runningSum(self, nums: List[int]) -> List[int]:
        """
        Input: nums = [1,2,3,4]
        Output: [1,3,6,10]
        Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
        """
        new_list = []
        for i in range(len(nums)):
            if len(new_list) == 0:
                new_list.append(nums[i])
            else:
                new_list.append(nums[i] + new_list[i - 1])
            # new_list[i] += nums[i]
        return new_list


if __name__ == "__main__":
    my_list = [3, 1, 2, 10, 1]
    solution = Solution()
    print(solution.runningSum(my_list))
