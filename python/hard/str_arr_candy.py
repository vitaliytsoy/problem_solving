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
from collections import deque
import sys 

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
        
        return sum(candies)
    
    
    # ---
    
    def find_sequence_streak(self, array, start):
        end = start
        sign = 0
        
        if start >= len(array) - 1:
            return [start, start, sign]
        
        if array[start + 1] > array[start]:
            sign = 1
            
            
        if array[start + 1] < array[start]:
            sign = -1
        
        for i in range(start + 1, len(array)):
            if sign == 0 and array[i] != array[end]:
                break
                    
            if sign == -1 and array[i] >= array[end]:
                break
                    
            if sign == 1 and array[i] <= array[end]:
                break
                           
            end = i
            
        
        
        return [start, end, sign]
    
    def candy(self, ratings: List[int]) -> int:
        candies = [0] * (len(ratings) + 2)
        curr = 0
        
        while curr < len(ratings):
            start, end, sign = self.find_sequence_streak(ratings, curr)
            
            if start == end: 
                if ratings[start] < ratings[start - 1]:
                    candies[start + 1] = 1
                    
                    if candies[start] == 1:
                        candies[start] += 1
                    
                if ratings[start] > ratings[start - 1]:
                    candies[start + 1] = candies[start] + 1
                    
                if ratings[start] == ratings[start - 1]:
                    candies[start + 1] = 1
                    
                curr = end + 1
                continue
            
            if sign == 0:
                for i in range(start, end + 1):
                    candies[i + 1] = 1
                    
                if start > 0 and ratings[start] > ratings[start - 1] and candies[start + 1] <= candies[start]:
                    candies[start + 1] = candies[start] + 1
                    
            if sign == 1:
                for i in range(start, end + 1):
                    if start == i and (ratings[start - 1] >= ratings[start]):
                        candies[i + 1] = 1
                    else:
                        candies[i + 1] = candies[i] + 1
                        
                if start > 0 and ratings[start - 1] > ratings[start] and candies[start] <= candies[start + 1]:
                    candies[start] = candies[start + 1] + 1
                    
            if sign == -1:
                for i in range(end, start - 1, -1):
                    candies[i + 1] = candies[i + 2] + 1
                    
                if start > 0 and ratings[start - 1] > ratings[start] and candies[start] <= candies[start + 1]:
                    candies[start] = candies[start + 1] + 1
            
            curr = end + 1

        return sum(candies)
    
    
        # ---
        
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candies[i - 1] = max(candies[i - 1], candies[i] + 1)
                
        return sum(candies)
        

        
s = Solution()
print(s.candy([1,0,2])) # 5 (2 1 2)
print(s.candy([1,2,2])) # 4 (1 2 1)
print(s.candy([1,2,3,4,5,6])) # 21 (1 2 3 4 5 6)
print(s.candy([1,2,3,1,0])) # 9  (1 2 3 2 1)
print(s.candy([1,2,3,4,5,5,5,5,4])) # 20 (1 2 3 4 5 1 1 2 1)
print(s.candy([1,2,3,1,2,1,3,3])) # 13  (1 2 3 1 2 1 2 1)
print(s.candy([1,2,87,87,87,2,1])) # 13  (1 2 3 1 3 2 1)
print(s.candy([1,6,10,8,7,3,2])) # 18  (1 2 5 4 3 2 1)
print(s.candy([2,3,2])) # 4 (1 2 1)
print(s.candy([4,2,3,4,1])) # 9 (2 1 2 3 1)
print(s.candy([1,2,3,5,4,3,2,1,4,3,2,1,3,2,1,1,2,3,4])) # 47 (1 2 3 5 4 3 2 1 4 3 2 1 3 2 1 1 2 3 4)
print(s.candy([58,21,72,77,48,9,38,71,68,77,82,47,25,94,89,54,26,54,54,99,64,71,76,63,81,82,60,64,29,51,87,87,72,12,16,20,21,54,43,41,83,77,41,61,72,82,15,50,36,69,49,53,92,77,16,73,12,28,37,41,79,25,80,3,37,48,23,10,55,19,51,38,96,92,99,68,75,14,18,63,35,19,68,28,49,36,53,61,64,91,2,43,68,34,46,57,82,22,67,89])) # 208 

# print(s.candy([56,82,584,683,750,131,239,296,372,920,671,691,239,7,784,888,285,795,783,994,804,716,632,870,223,764,257,294,440,429,731,848,511,315,883,614,447,123,262,171,43,933,862,282,292,646,171,577,794,306,923,598,23,555,469,598,671,78,893,111,507,624,960,370,291,843,336,738,966,598,910,9,884,124,292,528,771,815,458,565,121,733,163,496,641,984,95,312,62,340,424,921,316,384,292,607,579,628,698,546,579,608,907,815,84,199,343,855,366,801,772,840,535,288,336,528,272,783,840,687,123,264,608,439,0,900,47,580,881,97,126,460,57,33,275,141,585,970,997,303,772,121,143,659,409,832,187,682,615,27,721,739,644,329,530,644,230,929,224,111,26,702,923,83,88,198,225,25,168,574,328,292,695,472,303,457,656,842,491,271,222,212,362,866,541,893,862,123,822,439,586,201,493,509,284,581,59,861,606,580,787,935,224,835,759,880,292,767,722,783,38,944,995,401,162,888,646,377,12,820,168,598,21,661,460,306,243,519,519,201,451,307,488,676,494,599,556,786,366,630,569,405,927,916,158,441,804,804,818,816,624,986,767,998,648,227,656,243,98,175,444,550,834,285,578,328,884,486,114,251,116,35,656,43,303,166,485,108,322,655,276,298,642,43,296,642,622,952,237,721,128,33,623,314,318,201,643,203,687,109,454,155,145,462,199,448,980,36,908,302,691,185,600,685,580,897,679,203,201,916,276,681,950,899,996,620,452,639,823,491,100,629,646,597,91,197,398,71,233,306,725,277,843,326,962,424,575,994,979,776,262,255,458,564,154,806,185,958,797,360,449,897,990,95,495,433,293,893,857,878,551,582,155,395,260,470,171,835,464,150,964,78,757,774,643,911,580,828,221,729,540,670,626,530,117,473,964,410,366,821,641,270,403,796,665,664,618,188,851,434,338,167,513,95,941,508,358,873,336,579,602,228,601,581,759,718,54,723,481,421,896,122,43,651,270,708,315,889,248,519,675,586,686,188,33,980,696,743,205,384,674,808,613,275,389,724,345,795,447,826,216,695,300,611,346,571,319,14,812,567,533,487,505,571,28,890,903,76,633,109,461,659,269,426,934,10,150,632,805,949,458,374,644,111,985,990,682,657,356,846,576,241,333,82,813,713,324,68,790,958,177,603,969,446,29,904,808,531,888,614,480,346,988,476,457,973,818,491,630,175,337,207,768,23,641,581,88,965,2,878,275,179,481,245,978,862,501,786,745,389,400,577,87,740,53,897,714,224,740,696,751,430,903,519,453,896,453,893,862,455,772,489,634,605,734,964,820,587,103,565,976,503,143,416,596,548,313,310,772,53,358,523,483,262,395,288,510,848,182,724,303,306,214,289,911,300,254,731,888,357,649,864,212,792,632,808,340,945,470,465,351,829,988,186,443,735,475,953,583,9,678,886,315,892,176,578,192,782,662,80,139,311,297,703,455,929,512,795,227,982,612,578,163,953,116,606,688,591,560,272,952,238,510,619,482,686,550,26,820,212,459,311,875,756,15,330,37,879,477,616,213,90,194,377,43,311,983,83,254,895,355,559,485,866,178,967,904,80,346,725,292,805,36,519,913,403,201,950,282,679,567,496,121,113,873,516,776,208,599,383,104,307,294,589,525,472,909,429,553,255,506,197,412,543,69,325,946,270,627,581,949,546,77,422,12,302,290,788,510,890,523,966,549,817,908,74,642,169,503,547,776,362,96,188,905,165,513,203,436,492,784,737,39,213,512,51,515,802,191,378,44,715,344,593,532,252,667,526,421,523,73,197,885,170,385,142,335,250,697,123,95,834,861,134,47,373,185,563,175,728,941,572,443,637,165,328,890,185,854,663,60,280,213,297,450,950,791,137,201,488,261,648,322,474,782,370,199,319,285,726,47,578,298,843,215,816,171,457,1,377,121,413,657,334,62,459,284,853,597,837,341,210,485,664,36,619,386,235,938,671,961,338,249,612,181,816,428,704,274,781,81,395,546,91,81,608,550,365,461,499,555,802,709,392,818,97,12,204,332,950,227,646,288,828,258,821,645,686,525,919,819,607,666,365,698,747,973,600,464,434,100,19,588,161,412,407,259,776,963,591,726,543,589,367,723,847,540,368,885,66,639,704,25,305,421,723,404,394,675,869,180,775,240,769,937,4,528,196,780,843,139,859,738,729,578,462,928,118,830,814,536,822,870,561,127,644,636,884,38,312,753,571,87,993,692,376,350,572,924,130,415,64,341,154,145,919,968,73,38,150])) # 1974

