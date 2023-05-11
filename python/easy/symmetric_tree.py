# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
from typing import Optional
from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.check_nodes_symetric(root.left, root.right)
    
    def check_nodes_symetric(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        
        if (left and not right) or (right and not left):
            return False
        
        if left.val != right.val:
            return False;
        
        return self.check_nodes_symetric(left.left, right.right) and self.check_nodes_symetric(left.right, right.left)
        
    # --------------
    
    def isSymmetricMemoryIntensive(self, root: Optional[TreeNode]) -> bool:
        left_values = self.make_tree_values(root.left)
        right_values = self.make_tree_values(root.right, True)
        
        return left_values == right_values
    
    def make_tree_values(self, root: Optional[TreeNode], reverse: Optional[bool] = False):
        if (not root):
            return []
        
        values = []
        queue = deque([root])
        
        while (queue):
            node = queue.popleft()
            
            if (not node):
                values.append(None)
                continue;

            left = node.right if reverse else node.left
            right = node.left if reverse else node.right
            
            values.append(node.val)
            queue.append(left)
            queue.append(right)
                
        return values
    