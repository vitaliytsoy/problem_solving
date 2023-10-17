"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:

Input: digits = ""
Output: []

Example 3:

Input: digits = "2"
Output: ["a","b","c"]
"""
from typing import List

letter_map = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"],
}

class Solution:
    def backtrack(self, numbers, letters, i, result):
        number = numbers[i]

        if number not in letter_map:
            return

        input_letters = letter_map[number]
        
        for letter in input_letters:
            letters[i] = letter
            
            if i + 1 < len(numbers):
                self.backtrack(numbers, letters, i + 1, result)
            
            if (i == len(numbers) - 1):
                result.append(''.join(letters))
        
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        result = []
        
        self.backtrack(list(digits), [None] * len(digits), 0, result) 
        
        return result
