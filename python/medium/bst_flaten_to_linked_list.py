"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 
Example 1:

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [0]
Output: [0]
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverse(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if (node == None): 
            return node
        
        left_subtree = self.traverse(node.left)
        right_subtree = self.traverse(node.right)
        node.left = None
            
        if left_subtree and right_subtree:
            node.right = left_subtree
            
            while (left_subtree.right):
                left_subtree = left_subtree.right 
            
            left_subtree.right = right_subtree
        elif left_subtree:
            node.right = left_subtree
        elif right_subtree:
            node.right = right_subtree
            
        return node
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.traverse(root)
    