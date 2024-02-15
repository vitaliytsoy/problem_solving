"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.


Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions. 
"""
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [0] * len(ratings)
        candies[0] = 1
        before, curr = 0, 1
        
        while curr < len(ratings):
            if ratings[curr] < ratings[before]:
                if candies[before] - 1 == 0:
                    candies[curr] = 1
                    candies[before] += 1
                    
                    temp = curr
                    curr -= 1 
                    before -= 1
                    
                    while ratings[before] > ratings[curr] and candies[before] <= candies[curr] and before >= 0:
                        candies[before] += 1
                        before -= 1
                        curr -= 1
                        
                    curr = temp
                    before = curr - 1
                else:
                    candies[curr] = 1
            elif ratings[curr] == ratings[before]:
                candies[curr] = 1
            else: 
                candies[curr] = candies[before] + 1
                
            before = curr
            curr += 1
        
        print(candies)
        return sum(candies)

        
s = Solution()
# print(s.candy([1,0,2])) # 5 (2 1 2)
# print(s.candy([1,2,2])) # 4 (1 2 1)
# print(s.candy([1,2,3,4,5,6])) # 21 (1 2 3 4 5 6)
# print(s.candy([1,2,3,4,5,5,5,5,4])) # 20 (1 2 3 4 5 1 1 2 1)
# print(s.candy([1,2,3,1,2,1,3,3])) # 13  (1 2 3 1 2 1 2 1)
print(s.candy([1,2,3,1,0])) # 9  (1 2 3 2 1)


