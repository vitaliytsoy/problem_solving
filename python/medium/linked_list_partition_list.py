"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
"""
from typing import Optional
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = [], []
        pointer = head
        
        if head == None:
            return None
    
        while pointer.next:
            if pointer.val < x:
                left.append(pointer)
            else:
                right.append(pointer)
                
            pointer = pointer.next
            
        new_head = ListNode()
        
        if left:
            pointer = left[0]
            
            while pointer.next:
                new_head.next = pointer
                new_head = new_head.next
                pointer = pointer.next

        if right:
            pointer = right[0]
            
            while pointer.next:
                new_head.next = pointer
                new_head = new_head.next
                pointer = pointer.next
                
        return new_head.next