"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"
 
"""
from math import ceil 

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = numRows
        cols = ceil(len(s) / numRows)
        cols_with_diagonals = cols + (numRows - 2) * cols
        matrix = [['#' for _ in range(cols_with_diagonals)] for _ in range(rows)]
        is_up = False
        row = -1
        col = 0
        
        for i in range(len(s)):            
            if not is_up:
                row += 1
                matrix[row][col] = s[i]
            else:
                col += 1
                row -= 1
                matrix[row][col] = s[i]
            
            if row == len(matrix) - 1:
                is_up = True
                
            if row == 0:
                is_up = False
            
        result = ''
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '#':
                    continue
                
                result += matrix[i][j]
                
                
        return result
    
s = Solution()
print(s.convert("PAYPALISHIRING", 3)) # PAHNAPLSIIGYIR
print(s.convert("PAYPALISHIRING", 4)) # PINALSIGYAHRPI
print(s.convert("A", 2)) # A



# A     A
# A   A A
# A  A  A
# A A   A
# A     A

# 5 3