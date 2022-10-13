"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
 

Example 1:

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
"""
import re
from unittest import result

class Solution:
    def myAtoi(self, s: str) -> int:
        MIN_SIZE = - 2 ** 31
        MAX_SIZE = (-MIN_SIZE) - 1
        filtered_string = ''
        result = 0
        sign = 0

        for char in s:
            if char == " ":
                if len(filtered_string) > 0:
                    break;

                if sign != 0:
                    break

                continue

            if char == "+" or char == "-":
                if sign != 0 or len(filtered_string) > 0:
                    filtered_string = ''
                    break

                sign = 1 if char == "+" else -1
                continue

            if re.match(r"[^0-9]", char):
                break

            if sign == 0:
                sign = 1

            filtered_string += char 

        for i in range(1, len(filtered_string) + 1):
            result += int(filtered_string[-i]) * (10**(i-1))

            if (result >= MAX_SIZE + 1):
                return MAX_SIZE if sign == 1 else MIN_SIZE 

        return sign * result

solution = Solution()
# print(solution.myAtoi("42"))
# print(solution.myAtoi("   -42"))
# print(solution.myAtoi("4193 with 123 words"))
# print(solution.myAtoi("999999999"))
# print(solution.myAtoi("+-123"))
# print(solution.myAtoi("21474836460"))
# print(solution.myAtoi("  0000000000012345678"))
# print(solution.myAtoi("00000-42a1234"))
# print(solution.myAtoi("   +0 123"))
# print(solution.myAtoi("2147483648"))
print(solution.myAtoi("  +  413"))

