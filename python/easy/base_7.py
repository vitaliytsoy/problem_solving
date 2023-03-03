"""
Given an integer num, return a string of its base 7 representation.


Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"
"""
class Solution:
    def convertToBase7(self, num: int) -> str:
        result = ""

        if num == 0:
            return "0"
        
        if num < 0:
            return "-" + self.convertToBase7(-num)

        while num > 0:
            result += str(num % 7)
            num = int(num / 7)

        return result[::-1]
    

solution = Solution()
print(solution.convertToBase7(100))

