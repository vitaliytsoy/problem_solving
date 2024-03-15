"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, head: Optional[ListNode]):
        if head == None or head.next == None:
            return head
        
        before, pointer, after = None, head, head.next
        
        while pointer and pointer.next:
            pointer.next = before
            
            before = pointer
            pointer = after 
            after = pointer.next
            
        pointer.next = before
        
        return [pointer, head]
    

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:        
        if head == None or head.next == None: 
            return head
        
        if k == 1:
            return head
        
        new_head = ListNode()
        new_head.next = head
        
        before = new_head
        after = None
        pointer = head
        counter = 1
        
        while pointer:            
            if counter == k:
                after = pointer.next
                pointer.next = None
                
                new_h, new_t = self.reverse(before.next)
                
                before.next = new_h
                new_t.next = after
                
                pointer = after
                before = new_t
                counter = 1
                continue

            pointer = pointer.next
            counter += 1

        return new_head.next
                    