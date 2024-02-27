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


class Solution:
    operations = {'+', '-'}
    numbers = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    braces = {'(', ')', }
    
    def evaluate(self, a, op, b):
        return 0
    
    def calculate(self, s: str) -> int:
        pointer = 0
    
    
        num_a = 0
        operation = '+'
        num_b = 0
        
        #0 + ...s
        while pointer < len(s):
            char = s[pointer]
            
            if operation: 
                
                if char in self.number:
                    num_b = 
                # look for number
                if char in self.operations or
            else:
                # look for operation
            
            
            

            # if char in self.operations and op == '':
            #     # cases -1 -2 -    3 ...
            #     op = char
            #     pointer += 1
            #     continue
            
            # if char in self.braces:
            #     start = pointer
            #     end = pointer
                
            #     while end < len(s):
            #         if s[end] == ')':
            #             break
                    
            #         end += 1
                
            #     result += self.calculate(s[start:end])
            #     pointer = end + 1
            #     continue
        
            
            pointer += 1
    
        return result
    
s = Solution()
print(s.calculate("1 + 1")) # 2 
print(s.calculate(" 2-1 + 2 ")) # 3
print(s.calculate("(1+(4+5+2)-3)+(6+8)")) # 23
