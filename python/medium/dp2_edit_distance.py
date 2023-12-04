"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
 
"""
class Solution:
    def find_min_distance(self, word1, word2, memo):
        if word1 + word2 in memo:
            return memo[word1 + word2]
        
        if word1 == "":
            return len(word2)
        
        if word2 == "":
            return len(word1)
        
        if word1 == word2:
            return 0
        
        if word1[0] == word2[0]:
            return self.find_min_distance(word1[1:], word2[1:], memo)
        
        delete = 1 + self.find_min_distance(word1[1:], word2, memo)
        insert = 1 + self.find_min_distance(word1, word2[1:], memo)
        replace = 1 + self.find_min_distance(word1[1:], word2[1:], memo)
        
        memo[word1 + word2] = min(delete, insert, replace)

        return memo[word1 + word2]
    
    def minDistance(self, word1: str, word2: str) -> int:        
        return self.find_min_distance(word1, word2, {})
    
s = Solution()
print(s.minDistance("intention", "execution")) # 5
print(s.minDistance("horse", "ros")) # 3
print(s.minDistance("horse", "hello")) # 4
print(s.minDistance("", "")) # 0
print(s.minDistance("abc", "abc")) # 0
        
