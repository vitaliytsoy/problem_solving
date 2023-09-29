"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return head
        
        head_stub = ListNode(0, head)
        p_prev, p_cur =head_stub, head

        while p_cur:
            while p_cur.next and p_cur.val == p_cur.next.val:
                p_cur = p_cur.next
                
            if p_prev.next == p_cur:
                p_prev = p_prev.next
            else: 
                p_prev.next = p_cur.next
                
            p_cur = p_cur.next
            
        return head_stub.next
    
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return head
        
        p_prev, p_start, p_end = None, head, head.next
        
        while p_end:
            if (p_start.val == p_end.val):
                while p_end and p_end.val == p_start.val:
                    p_end = p_end.next
                    
                    
                if p_prev == None:
                    if p_end == None:
                        return None
                    
                    head = p_end
                    p_start = p_end
                    p_end = p_end.next
                else:
                    p_prev.next = p_end
                    
                    if (p_end == None):
                        return head
                    
                    p_start = p_end
                    p_end = p_end.next                    
            else:
                p_start = p_start.next
                p_end = p_end.next
                
                if (p_prev == None):
                    p_prev = head
                else:
                    p_prev = p_prev.next
                        
        return head
                        