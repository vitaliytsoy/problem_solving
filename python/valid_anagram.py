import re


class Solution:
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
    """
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}

        if len(s) != len (t): return False

        for i in range(0, len(s)):
            if s[i] not in dict_s:
                 dict_s[s[i]] = 1
            else:
                dict_s[s[i]] += 1

            if t[i] not in dict_t:
                dict_t[t[i]] = 1
            else:
                dict_t[t[i]] += 1

        if len(dict_s) != len(dict_t): return False


        for key in dict_s.keys():
            if key not in dict_t:
                return False

            if dict_t[key] != dict_s[key]:
                return False

        return True


    def isAnagramSimple() -> bool:
        s = sorted(s)
        t = sorted(t)
        
        return ''.join(s) == ''.join(t)




solution = Solution()

print(solution.isAnagram(s = "anagram", t = "nagaram"))