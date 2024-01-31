"""
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.

Example 1:

Input: root = [1,2,3,4,5,6]
Output: 6

Example 2:

Input: root = []
Output: 0

Example 3:

Input: root = [1]
Output: 1
"""
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    # ---
    
    def get_nodes_on_last_level(self, root, max_depth):
        queue = deque([(root, 0)])
        counter = 0
        
        while queue:
            node, depth = queue.popleft()
            
            if node == None:
                if depth == max_depth:
                    break
                else:
                    continue
            
            if depth == max_depth:
                counter += 1
                continue
            
            queue.append((node.left, depth + 1))
            queue.append((node.right, depth + 1))
                
        return counter
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
                     
        counter = 0
        max_depth = 0
        pointer = root
        
        while pointer.left:
            pointer = pointer.left
            max_depth += 1
            
        for depth in range(max_depth):
            counter += 2 ** depth
            
        counter += self.get_nodes_on_last_level(root, max_depth)
            
        return counter