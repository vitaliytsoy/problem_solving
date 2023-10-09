"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Example 1:

Input: root = [4,2,6,1,3]
Output: 1

Example 2:

Input: root = [1,0,48,null,null,12,49]
Output: 1
"""
from typing import Optional,List
from collections import deque
import sys

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverse(self, node: Optional[TreeNode], result: List[int], minimum: int):
        if node.left:
            left_min = self.traverse(node.left, result, minimum)
            minimum = min(left_min, minimum)
            
        if result:
            minimum = min(abs(result[-1] - node.val), minimum)
            
        result.append(node.val)
        
        if (node.right):
            right_min = self.traverse(node.right, result, minimum)
            minimum = min(right_min, minimum)
            
        return minimum
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # inorder traversal - left, root, right
        if root == None:
            return 0
        
        result = []
        
        return self.traverse(root, result, sys.maxsize)
