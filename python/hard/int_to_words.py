"""
Convert a non-negative integer num to its English words representation.

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
"""
class Solution:
    ones = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
    }
    tens = {
        0: 'zero',
        1: 'ten',
        2: 'twenty',
        3: 'thirty',
        4: 'fourty',
        5: 'fifty',
        6: 'sisxty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninty',
    }
    sizes = {
        2: "hundred",
        3: "thousand",
        6: "million",
        9: "billion"
    }
    plural = "s"


    def numberToWords(self, num: int) -> str:
        pass
        