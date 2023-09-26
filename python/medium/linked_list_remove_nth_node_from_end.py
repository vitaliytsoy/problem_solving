"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if (head == None):
            return None
        
        p1, p2 = None, head
        counter = 1
        
        # 1 - 2 - 3 - 4 - 5; 2 
        
        #|                |
        # 1 - 2 - 3 - 4 - 5; 5
        
        
        while p2.next:
            counter += 1
            
            if (counter > n):
                if (p1 == None):
                    p1 = head
                else:
                    p1 = p1.next
            
            p2 = p2.next
        
        if (p1 == None):
            return head.next
            
        p1.next = p1.next.next
        
        return head
        

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if (head == None):
            return None
        
        pointer = head
        length = 0
        
        while pointer:
            length += 1
            
            pointer = pointer.next
            
        if (n > length): 
            return head
        
        if (n == length):
            return head.next
        

        pointer = head
        prev_p = None
        counter = 0
        
        while counter + 1 <= length - n:
            counter += 1
            
            if (counter == length - n):
                prev_p.next = pointer.next
                pointer.next = None
                break
            
            prev_p = pointer
            pointer = pointer.next
            
        return head

            
        
            
            
            
            
    
        return head