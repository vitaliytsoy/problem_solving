"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
"""
# 10 30 40 50 70 80 90 ; k = 6


from operator import le
from typing import List
import random 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)
        left = []
        right = []
        mid = []

        # pivot = random.choice(nums)
        left =  [x for x in nums if x > pivot]
        mid  =  [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]

       left = []
        right = []
        mid = []
        print('-----', nums, k)
        print('pivot', pivot)
        print(left)
        print(mid)
        print(right)
        
        for num in nums:
            if num < pivot:
                if num in right:
                    continue
                right.append(num)
            elif num > pivot:
                if num in left:
                    continue
                left.append(num)
            else:
                if num in mid:
                    continue
                mid.append(num)

        print('-----', nums, k)
        print('pivot', pivot)
        print(left)
        print(mid)
        print(right)

        if len(left) >= k: 
            return self.findKthLargest(left, k)

        if len(left) + len(mid) < k:
            return self.findKthLargest(right, k - len(left) - len(mid))

        return mid[0]


solution = Solution()
# print('RESULT', solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4)) # 4
# print('RESULT', solution.test([3,2,1,5,6,4], 2)) # 4
# print('RESULT', solution.findKthLargest([3,2,1,5,6,4], 2)) # 5
# print(set(sorted([3,2,3,1,2,4,5,5,6])))
# print(sorted([3,2,1,5,6,4]))
print('RESULT', solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4)) # 4
print(set(sorted([3,2,3,1,2,4,5,5,6])))
