"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example 1:

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

Example 2:

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
"""
from typing import Optional
import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def find_max_sum(self, root: Optional[TreeNode], max_sum):
        left = 0
        right = 0
        left_max = -sys.maxsize
        right_max = -sys.maxsize
        
        if not root.left and not root.right:
            return (root.val, max(max_sum, root.val))
        
        if root.left:
            (new_left, left_max) = self.find_max_sum(root.left, max_sum)
            
            if new_left > 0:
                left = new_left
            
        if root.right:
            (new_right, right_max) = self.find_max_sum(root.right, max_sum)
            
            if new_right > 0:
                right = new_right
                
        root_max = root.val
        path_max = root.val + max(left, right)
        
        if right > 0: 
            root_max += right
            
        if left > 0:
            root_max += left

        return (path_max, max(max_sum, root_max, left_max, right_max))
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.find_max_sum(root, -sys.maxsize)[1]

