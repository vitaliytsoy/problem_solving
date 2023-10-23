"""
Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:

Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:

Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:

Input: head = []
Output: []
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
#         |           |       
# 1 2 3 4 5 6 7 8 9 10

class Solution:
    def mergesort(self, left_head, right_head):
        head = ListNode(0)
        p = head
        l_pointer = left_head
        r_pointer = right_head
        
        while l_pointer != None and r_pointer != None:
            if l_pointer.val < r_pointer.val:
                p.next = l_pointer
                l_pointer = l_pointer.next
            else:
                p.next = r_pointer
                r_pointer = r_pointer.next
                
            p = p.next
        
        if r_pointer != None:
            p.next = r_pointer
            r_pointer = r_pointer.next
            
        if l_pointer != None:
            p.next = l_pointer
            l_pointer = l_pointer.next
            
        return head.next
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        p1, p2 = head, head
        
        while p2 != None and p2.next != None:
            temp = p1
            p1 = p1.next
            p2 = p2.next.next
    
        temp.next = None
        left_head = self.sortList(head)
        right_head = self.sortList(p1)
        
        return self.mergesort(left_head, right_head)  
        