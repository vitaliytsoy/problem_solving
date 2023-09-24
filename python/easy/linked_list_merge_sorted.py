"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
"""
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def get_next_node(self, node_1: Optional[ListNode], node_2: Optional[ListNode]):
        if (node_1 == None):
            return node_2
        
        if (node_2 == None):
            return node_1
        
        if (node_1.val < node_2.val):
            return node_1
        
        return node_2
    
    def merge_two_lists_duplicate(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        head = None
        pointer = None
        
        if (list1 == None):
            return list2
        
        if (list2 == None):
            return list1
        
        while p1 or p2:
            node = self.get_next_node(p1, p2)
            
            if head == None:
                head = node
                pointer = head
            else:
                pointer.next = node
                pointer = pointer.next
                
            if p1 and node == p1:
                p1 = p1.next
                
            if p2 and node == p2:
                p2 = p2.next

        return head
    
    
    def get_next_node(self,  node1: Optional[ListNode], node2: Optional[ListNode]):
            if node1 == None and node2 == None:
                return None

            if node1 == None:
                return node2
            
            if node2 == None:
                return node1

            if node1.val < node2.val:
                return node1

            if node2.val < node1.val:
                return node2

            if node1.val == node2.val:
                return node1
        

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1_node = list1
        l2_node = list2
        head = None
        pointer = None
        next_node = self.get_next_node(l1_node, l2_node)

        if list1 == None: 
            return list2

        if list2 == None:
            return list1

        while next_node != None:
            if head == None:
                head = next_node

            if l1_node == next_node:
                l1_node = l1_node.next

            if l2_node == next_node:
                l2_node = l2_node.next

            if pointer != None:
                pointer.next = next_node
                pointer = next_node
            else:
                pointer = next_node

            next_node = self.get_next_node(l1_node, l2_node)
            
        return head
                
