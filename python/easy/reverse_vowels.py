class Solution:

    vowels = ['a', 'e', 'i', 'o', 'u']

    def reverseVowels(self, s: str) -> str:
        letters = list(s)
        start, end = 0, len(letters) - 1

        while start < end:
            skip = False

            print(start)
            print(end)

            if (letters[start] not in self.vowels):
                start += 1
                skip = True

            if (letters[end] not in self.vowels):
                end -= 1
                skip = True

            if (skip):
                continue

            letters[start], letters[end] = letters[end], letters[start]

            start += 1
            end -= 1

        pass

solution = Solution()

print(solution.reverseVowels('leetcode1'))
