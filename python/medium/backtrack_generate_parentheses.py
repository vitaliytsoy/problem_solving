"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]
"""
from typing import List

class Solution:
    def backtrack(self, combination, n, open_count, close_count, result):
        if len(combination) == n * 2:
            result.append(''.join(combination))
            return 
        
        if open_count < n:
            combination.append('(')
            self.backtrack(combination, n, open_count + 1, close_count, result)
            combination.pop()
            
        if close_count < open_count:
            combination.append(')')
            self.backtrack(combination, n, open_count, close_count + 1, result)
            combination.pop()
        
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        self.backtrack([], n, 0, 0, result)
        
        return result
    
s = Solution()

print(s.generateParenthesis(3)) # ["((()))","(()())","(())()","()(())","()()()"]
print(s.generateParenthesis(1)) # ["()"]