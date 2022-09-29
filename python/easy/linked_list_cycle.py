"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False

        p1 = p2 = head

        while p2 != None and p2.next != None:
            p1 = p1.next
            p2 = p2.next.next

            if p1 == p2:
                return True

        return False


    def has_cycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False

        unique = set()
        pointer = head

        while pointer.next != None:
            if pointer in unique:
                return True

            unique.add(pointer)

        return False
