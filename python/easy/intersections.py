"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
"""
from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(set(nums2)))

    def intersection_manual(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unique_nums_1= set(nums1)
        unique_nums_2= set(nums2)
        dict = {}

        for i in range(0, max(len(unique_nums_1), len(unique_nums_2))):

            if (len(unique_nums_1) > 0):
                value = unique_nums_1.pop()

                if value not in dict: 
                    dict[value] = 1
                else:
                    dict[value] += 1


            if (len(unique_nums_2) > 0):
                value = unique_nums_2.pop()

                if value not in dict: 
                    dict[value] = 1
                else:
                    dict[value] += 1

        result = []

        for key, value in dict.items():
            if (value > 1):
                result.append(key)

        return result



solution = Solution()

print(solution.intersection_manual([1,2,2,1,5], [2,2]))
