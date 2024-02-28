"""
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:

Input: s = "1 + 1"
Output: 2

Example 2:

Input: s = " 2-1 + 2 "
Output: 3

Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
"""
import re
from collections import deque

class Solution:
    operations = {'+', '-'}
    numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    braces = {'(', ')', }
    
    def evaluate(self, expression):
        numbers = deque(re.findall("([0-9]+)", expression))
        operations = deque(re.findall("(\+|\-)", expression))
        operation = '+'
        result = 0
        # 2-1 + 2 
        if not operations or not numbers:
            return 0
        
        if len(operations) > len(numbers) - 1:
            operation = operations.popleft()
        
        
        while numbers:
            number = int(numbers.popleft())
            
            if operation == '':
                operation = operations.popleft()
            
            if operation == '+':
                result += number
                
            if operation == '-':
                result -= number
                
            operation = ''
            
        return result
    
    def find_match_brace_index(self, expression, start):
        braces = []
        result = -1
        
        for i in range(start, len(expression)):
            char = expression[i]
            
            if char not in self.braces:
                continue

            if char == '(':
                braces.append('()')
                continue
                
            if char == ')' and braces[-1] == '()':
                result = i
                break
                
        return result
    
    def calculate(self, s: str) -> int:
        print('start', s)
        pointer = 0
        expression = ''

        if '(' not in s:
            return self.evaluate(s)
                
        while pointer < len(s):
            char = s[pointer]
            
            if char == ' ':
                pointer += 1
                continue
            
            if char == '(': 
                end_brace_index = self.find_match_brace_index(s, pointer)
                
                print(s, pointer, end_brace_index, s[pointer + 1:end_brace_index])
                
                if end_brace_index == -1:
                    break
                
                
                expression += str(self.calculate(s[pointer + 1:end_brace_index]))
                pointer = end_brace_index + 1
                
                continue
                
            expression += char
            pointer += 1
        
        return self.evaluate(expression)
    
s = Solution()


# print(s.evaluate(" 2-1 + 2 "))
# print(s.calculate("1 + 1")) # 2 
# print(s.calculate("-2 - 3")) # -5
# print(s.calculate("-2 + 4")) # 2
# print(s.calculate(" 2-1 + 2 ")) # 3

print(s.calculate("(1+(4+5+2)-3)+(6+8)")) # 23