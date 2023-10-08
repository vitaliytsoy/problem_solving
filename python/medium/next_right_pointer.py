"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Example 1:

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


Example 2:

Input: root = []
Output: []

"""

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        
from typing import Optional, List
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return None
        
        root.next = None
        
        if (root.left and root.right):        
            self.connect_nodes(self.link_nodes_list([root.left]), self.link_nodes_list([root.right]))
            
            root.left.next = root.right
            root.right.next = None

        return root
    
    def connect_nodes(self, l_nodes: List['Optional[Node]'], r_nodes: List['Optional[Node]']):
        if len(l_nodes) == 0 and len(r_nodes) == 0:
            return
        
        l_children = self.link_nodes_list(l_nodes)
        r_children = self.link_nodes_list(r_nodes)
        
        l_nodes[-1].next = r_nodes[0]
        
        self.connect_nodes(l_children, r_children)
    
    def link_nodes_list(self, nodes: List['Optional[Node]']):
        pointer = 0
        children = []
        
        while pointer < len(nodes) - 1:
            current_node = nodes[pointer]
            next_node = nodes[pointer + 1]  if (pointer + 1) < len(nodes) else None
            
            current_node.next = next_node
            
            if current_node.left:
                children.append(current_node.left)
                
            if current_node.right:
                children.append(current_node.right)
            
            pointer += 1
            
        return children
            
            