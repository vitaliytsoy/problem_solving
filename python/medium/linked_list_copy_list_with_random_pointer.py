"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

Example 1:

Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:

Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]

Example 3:

Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
"""
from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution: 
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if (head == Node):
            return None
        
        pointer = head
        
        while pointer:
            copy = Node(pointer.val, pointer.next)
            pointer.next = copy
            pointer = pointer.next.next
        
        pointer = head
        
        while pointer:
            if (pointer.random):
                pointer.next.random = pointer.random.next
            
            pointer = pointer.next.next
            
            
        p1 = head
        p2 = None
        new_head = None

        while p1:
            if (new_head == None):
                new_head = p1.next
                p2 = new_head
            else:
                p2.next = p1.next
                p2 = p2.next
            
            p1 = p1.next.next
                  
        return new_head
            
        
      
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if (head == None):
            return None
        
        p1 = head
        p2 = None
        head_copy = None
        pointer_links = {}
        
        while p1:
            if (head_copy == None):
                head_copy = Node(p1.val)
                p2 = head_copy
                pointer_links[p1] = p2
            else:
                p2.next = Node(p1.val)
                pointer_links[p1] = p2.next
                p2 = p2.next
            
            p1 = p1.next
        
        
        p1 = head
        p2 = head_copy
        
        while p1:
            if (p1.random and p1 in pointer_links):
                p2.random = pointer_links[p1.random]
            
            p1 = p1.next
            p2 = p2.next
            
        return head_copy
    
    