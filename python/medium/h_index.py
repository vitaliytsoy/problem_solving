"""
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

Example 1:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

Example 2:

Input: citations = [1,3,1]
Output: 1
"""
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        c_length = len(citations)
        bucket = [0] * (c_length + 1)
        
        
        for c in citations:
            if (c >= c_length):
                bucket[c_length] += 1
            else:
                bucket[c] += 1
        
        count = 0
    
        for i in range(c_length, 0, -1):
            count += bucket[i]
            
            print(bucket[i])
            print(count)
            print(bucket)
            print()
            
            if (count >= i):
                return i

        return 0
    
    def hIndex_own(self, citations: List[int]) -> int:
        citations.sort()
        h_index = 0
        
        if (len(citations) == 1):
            return min(citations[0], 1)
        
        for i in range(len(citations)):
            cit = citations[i]
            
            if (cit >= h_index):

                if (len(citations) - (i + 1) >= cit - 1):
                    h_index = cit
                else:
                    h_index = max(h_index, len(citations) - (i + 1) + 1)

        return h_index
    
    
s = Solution()
print(s.hIndex([3,0,6,1,5])) # 3
print(s.hIndex([1,3,1])) # 1
print(s.hIndex([100])) # 1
print(s.hIndex([11,15])) # 2
        