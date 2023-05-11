"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,2,3]

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
        
        
from typing import List, Optional
from collections import deque

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        stack = deque([root])
        result = []
        
        while (stack):
            node = stack.pop()
            
            if (node == None):
                continue;
            
            result.append(node.val)
            
            if (node.right):
                stack.append(node.right)
                
                
            if (node.left): 
                stack.append(node.left)

        return result