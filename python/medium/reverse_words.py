"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        split = s.split(' ')
        result = ''

        for index in range(1, len(split) + 1):
            word = split[-index]
            
            if len(word) == 0:
                continue

            result += f"{word} "

        return result.strip()

    def reverse_words(self, s: str) -> str:
        words = []
        word = ''

        for index, letter in enumerate(s):
            if len(word) == 0 and letter == ' ':
                continue

            if len(word) >= 1 and letter == ' ':
                words.append(word)
                word = ''

                continue
            
            word += letter

            if index == len(s) - 1:
                words.append(word)
                word = ''

        return ' '.join([words[index - 1] for index in range(len(words), 0, -1)])


solution = Solution()
# print(solution.reverseWords(" the sky   is blue  "))
# print(solution.reverse_words(" the sky   is blue  "))
# print(solution.reverse_words("the sky is blue"))
# print(solution.reverse_words("a good   example"))
print(solution.reverse_words(" asdasd df f"))
