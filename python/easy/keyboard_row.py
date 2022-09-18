"""
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example 2:

Input: words = ["omk"]
Output: []
"""
from typing import List

class Solution:
    keyboard_rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]

    def is_keyboard_row_word(self, word: str):
        normalized_word = word.lower()
        keyboard_row = list(row for row in self.keyboard_rows if normalized_word[0] in row)[0]

        for letter in normalized_word:
            if letter not in keyboard_row:
                return False

        return True

    def find_words(self, words: List[str]) -> List[str]:
        result = []

        for word in words:
            if self.is_keyboard_row_word(word):
                result.append(word)

        return result

solution = Solution();
print(solution.find_words(["Hello","Alaska","Dad","Peace"]))

# print(set("Alaska".lower()) <= set("asdfghjkl"))
