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
                braces.append('(')
                continue
                
            if char == ')' and braces[-1] == '(':
                braces.pop()

            if len(braces) == 0:
                result = i
                break
                
        return result
    
    def calculate(self, s: str) -> int:
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
                
                if end_brace_index == -1:
                    break
                
                expression += str(self.calculate(s[pointer + 1:end_brace_index]))
                pointer = end_brace_index + 1
                
                continue
                
            expression += char
            pointer += 1
            
        expression = expression.replace('--', '+')
        expression = expression.replace('+-', '-')
        
        return self.evaluate(expression)
    
s = Solution()


# print(s.evaluate(" 2-1 + 2 "))
# print(s.calculate("1")) # 1
# print(s.calculate("1 + 1")) # 2 
# print(s.calculate("-2 - 3")) # -5
# print(s.calculate("-2 + 4")) # 2
# print(s.calculate(" 2-1 + 2 ")) # 3
# print(s.calculate("(1+(4+5+2)-3)+(6+8)")) # 23
# print(s.calculate("1-(     -2)")) # 3
# print(s.calculate("5+3-4-(1+2-7+(10-1+3+5+(3-0+(8-(3+(8-(10-(6-10-8-7+(0+0+7)-10+5-3-2+(9+0+(7+(2-(2-(9)-2+5+4+2+(2+9+1+5+5-8-9-2-9+1+0)-(5-(9)-(0-(7+9)+(10+(6-4+6))+0-2+(10+7+(8+(7-(8-(3)+(2)+(10-6+10-(2)-7-(2)+(3+(8))+(1-3-8)+6-(4+1)+(6))+6-(1)-(10+(4)+(8)+(5+(0))+(3-(6))-(9)-(4)+(2))))))-1)))+(9+6)+(0))))+3-(1))+(7))))))))")) # -35
