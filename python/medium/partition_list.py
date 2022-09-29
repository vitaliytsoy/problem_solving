"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]

Constraints:

The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""
from typing import Optional, List
from xmlrpc.client import Boolean

# 1 - 4 - 3 - 2 - 5 - 2
# _ - + - + - _ - + - _

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def link_nodes(self, nodes: List[ListNode], return_last: Optional[bool] = False):
        length = len(nodes)

        for i in range(0, length):
            if i + 1 >= length:
                nodes[i].next = None

                continue

            nodes[i].next = nodes[i+1] 

        return nodes[length - 1] if return_last else nodes[0]

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        pointer = head
        greater = []
        lesser = []

        while pointer != None:
            if pointer.val < x:
                lesser.append(pointer)
            else:
                greater.append(pointer)

            pointer = pointer.next

        if len(lesser) == 0 or len(greater) == 0:
            return head


        self.link_nodes(lesser, True).next = self.link_nodes(greater)
    
        return lesser[0]
            
        