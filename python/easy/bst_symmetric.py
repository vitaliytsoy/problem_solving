"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center). 

Example 1:

Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

Input: root = [1,2,2,null,3,null,3]
Output: false
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def check_is_symmetric(self, node_a, node_b):
        if node_a == None and node_b == None:
            return True
        
        if node_a == None or node_b == None:
            return False
        
        if node_b.val != node_b.val:
            return False
        
        return self.check_is_symmetric(node_a.left, node_b.right) and self.check_is_symmetric(node_a.right, node_b.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
           
        return self.check_is_symmetric(root.left, root.right)
        