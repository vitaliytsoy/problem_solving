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

    
        while pointer:
            if pointer.val < x:
                left.append(pointer)
            else:
                right.append(pointer)
                
            pointer = pointer.next

        new_head = ListNode()
        pointer  = new_head

        if left:
            for node in left:
                pointer.next = node
                pointer = pointer.next

        if right:
            for node in right:
                pointer.next = node
                pointer = pointer.next

        pointer.next = None

        return new_head.next
    
    # ---

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode(0)
        right = ListNode(0)
        p1, p2 = left, right

        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next

            head = head.next
        
        p2.next = None
        p1.next = right.next
        right.next = None

        return left.next