"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

 

Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count("1")
    
    def hamming_distance(self, x: int, y: int) -> int: 
        x_bin = bin(x)[2:]
        y_bin = bin(y)[2:]
        distance = 0
        
        for i in range(1, 32):
            x_bit = "0" if i > len(x_bin) else x_bin[-i]
            y_bit = "0" if i > len(y_bin) else y_bin[-i]
            
            if (x_bit != y_bit):
                distance += 1
            
        return distance
    
s = Solution()
# s.hammingDistance(1, 4)
print(s.hamming_distance(1, 4))
print(s.hamming_distance(0, 1))
