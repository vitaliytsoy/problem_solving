"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
"""
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def traverse(self, node: Optional[TreeNode], result) -> List[TreeNode]:
        if node.left:
            self.traverse(node.left, result)
            
        result.append(node.val)
        
        if node.right:
            self.traverse(node.right, result)
            
        return result
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root == None:
            return 0
        
        result = []
        
        self.traverse(root, result)
        
        return result[k - 1]
        
