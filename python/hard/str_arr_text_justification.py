"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

"""
from typing import List
from collections import deque

class Solution:
    def get_justified_spaces(self, spaces_amount, dividers_count):
        if dividers_count == 0:
            dividers_count = 1 
        
        spaces = deque([''] * dividers_count)
        pointer = 0
                
        for i in range(spaces_amount): 
            spaces[pointer] += ' '
            
            if pointer == dividers_count - 1:
                pointer = 0
            else:
                pointer += 1
        
        return spaces
    
    def justify(self, words: List[str], maxWidth: int, result: List[str]):
        line_words = deque([])
        total_length = 0
        
        if len(words) == 0:
            return result
        
        for i in range(len(words)):
            word = words[i]
        
            if total_length + len(word) > maxWidth:
                break
            
            line_words.append(word)
            total_length += len(word) + 1

        words_used = len(line_words)
        total_length = total_length - len(line_words)        
        fill_spaces = self.get_justified_spaces(maxWidth - total_length, len(line_words) - 1)
        result_line = ''
        
                    
        if len(line_words) == len(words):
            result_line += " ".join(line_words)
            
            for i in range(maxWidth - len(result_line)):
                result_line += " "
                
            result.append(result_line)
            
            return result

        
        while line_words:
            result_line += line_words.popleft()
            
            if fill_spaces:
                result_line += fill_spaces.popleft()
                
        result.append(result_line)
                
        return self.justify(words[words_used:], maxWidth, result)
        
    
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []

        return self.justify(words, maxWidth, result)
            
            
            
        
    
s = Solution()
print(s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(s.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
print(s.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))

    
    