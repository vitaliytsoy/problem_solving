"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        str_1 = []
        str_2 = []

        for i in range(0, max(len(s), len(t))):
            if i < len(s):
                if s[i] == "#":
                    if len(str_1) != 0:
                        str_1.pop(-1)
                else:
                    str_1.append(s[i])


            if i < len(t):
                if t[i] == "#":
                    if len(str_2) != 0:
                        str_2.pop(-1)
                else:
                    str_2.append(t[i])

        return ''.join(str_1) == ''.join(str_2)



solution = Solution()


# print('STR1', solution.backspaceCompare("ab#c", "ad#c"))
# print('STR1', solution.backspaceCompare("ab##", "c#d#"))
# print('STR1', solution.backspaceCompare("a#c", "b"))
# print('STR1', solution.backspaceCompare("a##c", "#a#c"))
print('STR1', solution.backspaceCompare("xywrrmp", "xywrrmu#p"))


# "xywrrmp"
# "xywrrmu#p"