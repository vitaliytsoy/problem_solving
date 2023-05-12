"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]


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


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        
        result = []
                
        return self.traverse(root, result) 
    
    def traverse(self, node, result):
        if (node.left):
            self.traverse(node.left, result)
            
        result.append(node.val)
        
        if (node.right):
            self.traverse(node.right, result)
            
        return result
        