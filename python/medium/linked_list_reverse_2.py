"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev_node, current_node, next_node  = None, head, head.next
        
        while current_node:
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            
            if (next_node != None):
                next_node = current_node.next
            
        return {
            "end": head,
            "start": prev_node,
        }
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return head
        
        start_node = head
        end_node = None
        pointer = head
        counter = 1
        
        while pointer:
            if (counter == left - 1):
                start_node = pointer
            elif (counter == right):
                end_node = pointer.next
                pointer.next = None
                break
                                    
            counter += 1
            pointer = pointer.next
            
        reversed_list = self.reverseList(head if left == 1 else start_node.next)
        start_node.next = reversed_list["start"]
        reversed_list["end"].next = end_node
        
        return reversed_list["start"] if left == 1 else head