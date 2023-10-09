"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
"""
from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# [0] False
# [2, 3] True [2, 3]
# [4,5,6,7] False [4,5,6,7]
# [8,9,10,11,12,13,14,15]

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        queue = deque([root])
        result = []
        is_reverse = False
        
        while queue:
            length = len(queue)
            level = []

            for i in range(length):
                index = length - 1 - i if is_reverse else i
                node = queue.popleft()
                level[index] = node.val
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
            result.append(level)
            is_reverse = not is_reverse
            
        return result
            
        