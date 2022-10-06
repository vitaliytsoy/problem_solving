"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
"""
from math import floor
from heapq import heapify, heappush, heappop
import sortedcontainers

class MedianFinder:
    def __init__(self):
        self.min_pq = []
        self.max_pq = []

    def addNum(self, num: int) -> None:
        heappush(self.max_pq, -num)
        heappush(self.min_pq, -heappop(self.max_pq))

        if len(self.min_pq) > len(self.max_pq):
            heappush(self.max_pq, -heappop(self.min_pq))
            

    def findMedian(self) -> float:
        l_min = len(self.min_pq)
        l_max = len(self.max_pq)

        if l_max > l_min:
            return -self.max_pq[0]

        if l_max < l_min:
            return self.min_pq[0]

        return (-self.max_pq[0] + self.min_pq[0]) / 2


# class MedianFinder:
#     def __init__(self):
#         self.container = sortedcontainers.SortedList();

#     def addNum(self, num: int) -> None:
#         self.container.add(num)

#     def findMedian(self) -> float:
#         l = len(self.container)

#         if l % 2 == 0:
#             middle_index = int(len(self.container) / 2)

#             return (self.container[middle_index] + self.container[middle_index - 1]) / 2

#         return self.container[floor(len(self.container) // 2)]


obj = MedianFinder()
obj.addNum(1)
print('Median', obj.findMedian())
obj.addNum(2)
print('Median', obj.findMedian())
obj.addNum(3)
print('Median', obj.findMedian())
obj.addNum(4)
print('Median', obj.findMedian())
obj.addNum(5)
print('Median', obj.findMedian())



# obj.addNum(-1)
# print('Median', obj.findMedian())
# obj.addNum(-2)
# print('Median', obj.findMedian())
# obj.addNum(-3)
# print('Median', obj.findMedian())
# obj.addNum(-4)
# print('Median', obj.findMedian())
# obj.addNum(-5)
# print('Median', obj.findMedian())
# -1.00000
# -1.50000
# -2.00000
# -2.50000
# -3.00000