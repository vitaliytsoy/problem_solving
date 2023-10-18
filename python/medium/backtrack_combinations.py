"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
"""
from typing import List

class Solution:
    def backtrack(self,
        combination: List[int],
        n: int,
        k: int,
        prev: int,
        result: List[List[int]],
    ):
        if len(combination) == k:
            result.append(combination.copy())
            
            return 

        for number in range(prev, n + 1):
            if (number in combination):
                continue
            
            combination.append(number)
            
            self.backtrack(combination, n, k, number, result) 
            
            combination.pop()
        
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        self.backtrack([], n, k, 1, result)
        
        return result
    
s = Solution()
print(s.combine(4, 2))
# print(s.combine(10, 7))
# print(s.combine(20, 10))
