"""
Given two binary strings a and b, return their sum as a binary string.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        p1 = len(a)
        p2 = len(b)
        remainder = False
        result = ''
        
        while p1 > 0 or p2 > 0:
            p1 -= 1
            p2 -= 1
            bit_a = '0' if  p1 < 0 else a[p1]
            bit_b = '0' if  p2 < 0 else b[p2]
            
            if bit_a == '1' and bit_b == '1':
                if remainder:
                    result += '1'
                else:                    
                    result += '0'
                    
                remainder = True
                continue
                    
            if bit_a == '1' or bit_b == '1':
                if remainder:   
                    result += '0'
                else:
                    result += '1'
                    remainder = False
                continue
                
            if remainder:
                result += '1'
                remainder = False
            else:
                result += '0'
                
        if remainder:
            result += '1'
            
            
        return ''.join(reversed(list(result)))
            
            
            
            
s = Solution()
print(s.addBinary("11", "1")) # 100
print(s.addBinary("1010", "1011")) # 10101