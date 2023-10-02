"""
Given the head of a linked list, rotate the list to the right by k places.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (head == None or head.next == None or k == 0):
            return head 

        pointer = head
        length = 1
        
        while pointer:                
            if pointer.next == None:
                pointer.next = head
                break
                
            length += 1
            pointer = pointer.next
        
        k = k % length
        temp = head    
        
        for _ in range(length - k - 1):
            temp = temp.next
            
        
        new_head = temp.next
        temp.next = None
        
        return new_head
