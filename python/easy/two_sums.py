"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

"""
a + b = target

target - b = a
a OR b > target - Invalid values 
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # normalized_nums = sorted(set(nums))
        dict = {}

        for index, num in enumerate(nums):
            if num >= target: 
                continue

            if num in dict.keys():
                second_index = dict.get(num)

                return [index, second_index]

            dict[target - num] = index


        return []



        pass


solution = Solution()

solution.twoSum([2,4,5], 9);