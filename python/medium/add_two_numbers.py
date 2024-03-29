"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 
Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]


Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root = ListNode(0)
        pointer = root
        value = 0
        remainder = 0
        
        while l1 or l2 or remainder:
            if (l1):
                value += l1.val
                        
            if (l2):
                value += l2.val
                
            value += remainder
            pointer.val = value % 10
            remainder = value // 10
            value = 0
            
            if (l1): 
                l1 = l1.next
                
            if (l2): 
                l2 = l2.next
                
            if (l1 or l2 or remainder):
                pointer.next = ListNode(0)
                pointer = pointer.next
                
        return root
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = 0
        root = ListNode(0)
        pointer = root
        remainder = 0
         
        while l1 or l2 or remainder == 1:
            if (l1):
                sum += l1.val

            if (l2): 
                sum += l2.val

            sum += remainder
            
            pointer.next = ListNode(sum % 10)
            pointer = pointer.next
            
            remainder = sum // 10
            sum = 0
            
            if (l1):
                l1 = l1.next    

            if (l2):
                l2 = l2.next

        return root.next
    