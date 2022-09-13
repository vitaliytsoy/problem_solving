"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
"""
class Solution:
    def isValid(self, s: str) -> bool:
        start = {
            "(": 1,
            "{": 2,
            "[": 3
        }
        end = {
            ")": 1,
            "}": 2,
            "]": 3 
        }
        stack = []

        for bracket in s:
            if bracket in start:
                stack.append(start[bracket])

                continue;

            if len(stack) == 0:
                return False

            if bracket in end and stack[-1] == end[bracket]:
                stack.pop(-1)
            else:
                return False

        return len(stack) == 0
                
        

solution = Solution()
print(solution.isValid("()[]{}"))
print(solution.isValid("([]){}"))
print(solution.isValid("]"))



# a = list('qwerty')
# print(a[:-1])
# a.pop(-1)

# print(a)

