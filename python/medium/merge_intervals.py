from filecmp import cmp
from typing import List

class Solution:
    def is_overlaps(self, left: List[int], right: List[int]) -> bool:
        return (right[1] <= left[1] and right[1] >= left[0]) \
            or (left[1] >= right[0] and left[1] <= right[1])

    def merge_intervals(self, left: List[int], right: List[int]) -> List[int]:
        return [left[0], max(left[1], right[1])]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        i = 1

        if len(intervals) == 1: 
            return intervals


        while i < len(sorted_intervals):
            if (i >= len(sorted_intervals)):
                break

            previous=sorted_intervals[i-1]
            current=sorted_intervals[i]

            if (self.is_overlaps(previous, current)):
                sorted_intervals[i-1] = self.merge_intervals(previous, current)
                sorted_intervals.pop(i)
            else: 
                i += 1

        return sorted_intervals

                
        

        # for i in range(1, len(sorted_intervals)):
        #     if (i >= len(sorted_intervals)):
        #         break

        #     previous=sorted_intervals[i-1]
        #     current=sorted_intervals[i]

        #     if (self.is_overlaps(previous, current)):
        #         print("INDEX: ", i)

        #         sorted_intervals[i-1] = self.merge_intervals(previous, current)
        #         sorted_intervals.pop(i)

                

            # print("INDEX", i)

        


        # if len(intervals) == 1: 
        #     return intervals


        # for i in range(1, len(sorted_intervals)):
        #     previous=sorted_intervals[i-1]
        #     current=sorted_intervals[i]

        #     print()
        #     print(previous)
        #     print(current)

        #     if current == previous or is_merged:
        #         is_merged = False

        #         result.append(current)
        #         print('CONTINUE')
        #         continue

        #     print(f"{current[0]} <= {previous[1]}")
        #     if current[0] <= previous[1]:
        #         merged = self.merge_intervals(previous, current)
        #         merge_counter += 1


        #         if len(result) == 0 or result[-1] != merged:
        #             is_merged = True

        #             result.append(merged)
        #             print('MERGED', merged)

        #         # result.append(merged)
        #         # print('MERGED', merged)

        #     else: 
        #         if len(result) == 0 or result[-1] != previous:
        #             result.append(previous)
        #             print('PUSHED', previous)

        #         result.append(current)
        #         print('PUSHED', current)


        # print('MERGE COUNT:', merge_counter)
        # print('RESULT:', result)

        # if merge_counter > 0:
        #     return self.merge(result)

        # return result

solution = Solution()

# print('SOLUTION: ', solution.merge([[8,10], [1,3], [2,6], [15,18], [14,19]]))
# print('SOLUTION: ', solution.merge([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]))
# print('SULUTION', solution.merge([[1,4],[0,2],[3,5]]))
# print('SULUTION', solution.merge([[1,4],[4,5]]))
# print('SOLUTION', solution.merge([[1,4],[0,0]]))