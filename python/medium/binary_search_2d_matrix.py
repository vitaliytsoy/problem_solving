"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        start = 0
        end = m * n - 1
        
        while start <= end:
            middle = (start + end) // 2
            num = matrix[middle // m][middle % m]
            
            if target == num: 
                return True
            
            if target < num:
                end = middle - 1
            else:
                start = middle + 1
        
        return False
    
    
    def find_row(self, matrix, target):
        start = 0
        end = len(matrix) - 1
        row_length = len(matrix[0])
        
        while start <= end: 
            middle = (start + end) // 2
            first_num = matrix[middle][0]
            last_num = matrix[middle][row_length - 1]
            
            if target >= first_num and target <= last_num:
                return middle
            
            if target < first_num:
                end = middle - 1
                
            if target > last_num:
                start = middle + 1
                
        return -1
    
    def find_index(self, row, target):
        start = 0
        end = len(row) - 1
        
        while start <= end:
            middle = (start + end) // 2
            num = row[middle]
            
            if num == target:
                return middle
            
            if num < target:
                start = middle + 1
                
            if num > target:
                end = middle - 1
                
        return -1
    
    def searchMatrix1(self, matrix: List[List[int]], target: int) -> bool:
        row_index = self.find_row(matrix, target)
        
        if (row_index == -1):
            return False
        
        num_index = self.find_index(matrix[row_index], target)
        
        print(num_index)
        return True if num_index != -1 else False

    
s = Solution()
# print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)) # true
# print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)) # false
# print(s.searchMatrix([[1]], 2)) # false
# print(s.searchMatrix([[1,3]], 3)) # true
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 5)) # true


