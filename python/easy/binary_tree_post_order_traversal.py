"""
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [1]
Output: [1]
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional, List
from collections import deque


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        result = []
                
        return self.traverse(root, result) 
    
    def traverse(self, node, result):
        if (node.left):
            self.traverse(node.left, result)
        
        if (node.right):
            self.traverse(node.right, result)
    
        result.append(node.val)
            
        return result
        