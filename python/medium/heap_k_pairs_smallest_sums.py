"""
You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
"""
from typing import List
from collections import deque
import itertools
import heapq

#    |       |
# [1,3,5] [2,5,6]
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        queue = []
        visited = set()
        
        heapq.heappush(queue, (nums1[0] + nums2[0] , 0, 0))
        
        while queue and len(result) < k:
            _, i, j = heapq.heappop(queue)
            
            if ((i, j) in visited):
                continue
            
            result.append([nums1[i], nums2[j]])
            visited.add((i, j))

            if i + 1 < len(nums1): 
                heapq.heappush(queue, (nums1[i + 1] + nums2[j], i + 1, j))
                
            if j + 1 < len(nums2): 
                heapq.heappush(queue, (nums1[i] + nums2[j + 1], i, j + 1))
                
        return result

    
s = Solution()
print(s.kSmallestPairs([1,2], [3], 3)) # [[1,3],[2,3]]
print(s.kSmallestPairs([1,1,2], [1,2,3], 2)) # [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
print(s.kSmallestPairs([1,7,11], [2,4,6], 3)) # [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
print(s.kSmallestPairs([1,2,4,5,6], [3,5,7,9], 3)) # 

#    3  5  7  9
# 1  4  6  8  10
# 2  5  7  9  11
# 4  7  9  11 13
# 5  8  10 12 14
# 6  9  11 13 15