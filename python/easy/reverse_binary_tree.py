# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if (not root):
            return root
        
        self.switch_nodes(root)
        
        if (root.right):
            self.invertTree(root.right)
            
        if (root.left):
            self.invertTree(root.left)

        return root
            
    
    def switch_nodes(self, node: TreeNode):
        node.left, node.right = node.right, node.left
        
        return node