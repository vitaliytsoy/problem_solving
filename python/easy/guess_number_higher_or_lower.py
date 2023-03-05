"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

Example 1:

Input: n = 10, pick = 6
Output: 6

Example 2:

Input: n = 1, pick = 1
Output: 1

Example 3:

Input: n = 2, pick = 1
Output: 1
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

def guess(num: int) -> int:
    guess = 10
    
    if num == guess:
        return 0
    
    if num > guess:
        return -1
    
    if (num < guess):
        return 1
    
import math

class Solution:
    def guessNumber(self, n: int) -> int:
        max = n
        min = 1
        
        while True:
            guess_num = math.floor(max / 2) + math.ceil(min / 2)
            result = guess(guess_num)
            
            if (result == 0):
                break

            if (result == 1):
                min = guess_num
                
                if (max - min == 1):
                    guess_num = max
                    break

            if (result == -1): 
                max = guess_num 
    
                if (max - min == 1):
                    guess_num = min
                    break
                
        return guess_num
    
s = Solution()
print(s.guessNumber(10))
