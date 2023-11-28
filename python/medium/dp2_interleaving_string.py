"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where s and t are divided into n and m 
substrings
 respectively, such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Explanation: One way to obtain s3 is:
Split s1 into s1 = "aa" + "bc" + "c", and s2 into s2 = "dbbc" + "a".
Interleaving the two splits, we get "aa" + "dbbc" + "bc" + "a" + "c" = "aadbbcbcac".
Since s3 can be obtained by interleaving s1 and s2, we return true.

Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Explanation: Notice how it is impossible to interleave s2 with any other string to obtain s3.

Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_dp = [0] * len(s1)
        s2_dp = [0] * len(s2)
        s3_dp = [0] * len(s3)
        
        if len(s3) == 0:
            return True
        
        if (s3[0] != s1[0] and s3[0] != s2[0]):
            return False
        
        s1_p = 0
        s2_p = 0
        s1_dp[0] = 1
        
        for (index, letter) in enumerate(s3):
            
            print(s1_p)
            print(s2_p)
            

            if s1_p < len(s1) and letter == s1[s1_p]:
                s3_dp[index] = 's1'
                s1_p += 1
                
            elif s2_p < len(s2) and letter == s2[s2_p]:
                s3_dp[index] = 's2'
                s2_p += 1
                
            # print(s1_dp)
            # print(s2_dp)
            print(s3_dp)
            # print('===')
                
        return sum(s3_dp) == len(s3)
                
    
s = Solution()
print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac")) # true
# print(s.isInterleave("aabcc", "dbbca", "aadbbbaccc")) # false
# print(s.isInterleave("aacde", "bbcdy", "aabbccddee")) # false
# print(s.isInterleave("", "", "")) # true