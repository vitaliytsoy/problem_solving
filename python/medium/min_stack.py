"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
"""
from typing import List

class MinStack:
    container: List[int]
    min_val: int

    def __init__(self):
        self.container = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if (not self.min_stack or val <= self.getMin()):
            self.min_stack.append(val)
        
        self.container.append(val)

    def pop(self) -> None:
        removed = self.container.pop()
        
        if (removed == self.getMin()):
            self.min_stack.pop()

    def top(self) -> int:
        return self.container[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

s = MinStack()

print(s.push(-2)) 
print(s.push(0))
print(s.push(-3))
print(s.push(-3))
print(s.getMin()) # -3
print(s.pop())
print(s.top()) # 0
print(s.getMin()) # -2