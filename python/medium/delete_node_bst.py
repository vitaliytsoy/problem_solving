"""
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
 

Example 1:

Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Example 3:

Input: root = [], key = 0
Output: []
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from collections import deque
        
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None
        
        if (key > root.val):
            root.right = self.deleteNode(root.right, key)
        elif (key < root.val):
            root.left = self.deleteNode(root.left, key)
        else:
            if (root.left == None):
                return root.right
            
            if (root.right == None):
                return root.left
            
            if (root.right and root.left):
                temp = root.right
                
                while temp.left: temp = temp.left
                
                root.val = temp.val
                root.right = self.deleteNode(root.right, root.val)
        return root
    
    def deleteNodeIterative(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None
                
        node, parent = self.find_node(root, key)

        if (node):
            if node.right == None:
                if (parent.left == node):
                    parent.left = node.left
                    
                if (parent.right == node):
                    parent.right = node.left

                return root
            elif node.left == None:
                if (parent.left == node):
                    parent.left = node.right
                    
                if (parent.right == node):
                    parent.right = node.right

                return root
            else:
                # find successor
                # replace with successor
                return root

        return root
    
    def find_node(self, root: Optional[TreeNode], value: int) -> Optional[TreeNode]:
        pointer = root
        stack = deque([])
        
        while stack or pointer:
            while pointer:
                stack.append(pointer)
                pointer = pointer.right
                
            node = stack.pop()
            pointer = node.right
            
            if (node.val == value):
                return  [node, stack.pop()]
            
            return None
        
        
        
        