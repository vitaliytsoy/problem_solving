"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []
"""
from typing import List, Optional
import sys

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new_head = ListNode()
        pointer = new_head
        
        while lists:
            min_node = None
            min_node_index = -1
            
            for i in range(len(lists)):
                node = lists[i]
                
                if node and min_node:
                    if node.val <= min_node.val:
                        min_node = node
                        min_node_index = i
                    continue
                
                if min_node_index == -1:
                    min_node = node
                    min_node_index = i 

                        
            if min_node_index != -1 and min_node == None:
                lists.pop(min_node_index)
                continue
        
            if min_node.next == None:
                lists.pop(min_node_index)
            else:
                lists[min_node_index] = lists[min_node_index].next
 
            pointer.next = min_node
            pointer = pointer.next
            pointer.next = None
            
        return new_head.next
    
    
    
def convertIntListToNodeList(int_list):
    for i in range(len(int_list)):
        l = int_list[i]
        h = ListNode()
        p = h
        
        for j in range(len(l)):
            n = l[j]
            new_node = ListNode(n)
            p.next = new_node
            p = p.next
        
        int_list[i] = h.next
    
    return int_list
    
def print_nodes(node):
    p = node
    string = '';
    
    while p:
        string += f"{p.val} "
        p = p.next
        
    print(string)
    
        
s = Solution()
print_nodes(s.mergeKLists(convertIntListToNodeList([[],[-1,5,11],[],[6,10]])))
print_nodes(s.mergeKLists(convertIntListToNodeList([[2],[],[-1]])))
print_nodes(s.mergeKLists(convertIntListToNodeList([[1,4,5],[1,3,4],[2,6]])))

        


        
        
        
        