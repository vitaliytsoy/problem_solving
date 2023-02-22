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
        0: 'Zero',
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen',
    }
    tens = {
        0: '',
        1: 'Ten',
        2: 'Twenty',
        3: 'Thirty',
        4: 'Forty',
        5: 'Fifty',
        6: 'Sixty',
        7: 'Seventy',
        8: 'Eighty',
        9: 'Ninety',
    }
    sizes = {
        2: "Hundred",
        3: "Thousand",
        6: "Million",
        9: "Billion"
    }
    plural = "s"

    def makeNthDigit(self, num: int, digit: int) -> str:
        if digit == 1:
            return self.ones[num]

        if digit == 10: 
            return self.tens[num]

        if digit == 100:
            return f'{self.ones[num]} {self.sizes[2]}'

        return ''


    def numberToWords(self, num: int) -> str:
        groups = []
        unit = []
        result = ''

        if num == 0:
            return self.makeNthDigit(num, 1)

        while num >= 0:
            if len(unit) == 3 or num == 0:
                groups.append(unit)

                unit = []

            if num == 0:
                unit.append(0)
                break;

            unit.append(num % 10)
            num = num // 10

        for (index, group) in enumerate(groups):
            skip = False;

            if sum(group) == 0:
                continue

            for (i, n) in enumerate(group):
                modifyer = '';

                print(result)
                
                if skip:
                    skip = False;

                    continue;

                if i == 0: 
                    if index == 1:
                        modifyer = self.sizes[3]

                    if index == 2:
                        modifyer = self.sizes[6]

                    if index == 3:
                        modifyer = self.sizes[9]

                    result = modifyer + ' ' + result

                if n == 0:
                    continue


                if i == 0 and len(group) >= 2:
                    s = group[0] + group[1] * 10

                    if s >= 11 and s <= 19:
                        result = self.makeNthDigit(s, 10 ** i) + ' ' + result
                        skip = True

                        continue;

                result = self.makeNthDigit(n, 10 ** i) + ' ' + result


            # print(index)
            print(group)
            

        # print(result)
        print(groups)
        # print(str(num))
        return result


s = Solution()
# s.makeNthDigit(5, 1)
print(s.numberToWords(1000000))
print(sum([1,2,3]))
# s.numberToWords(12345)
# s.numberToWords(11234567)

        