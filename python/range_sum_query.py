from typing import List

class NumArray:
    """
    Given an integer array nums, handle multiple queries of the following type:

    Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
    Implement the NumArray class:

    NumArray(int[] nums) Initializes the object with the integer array nums.
    int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
    """
    def __init__(self, nums: List[int]):
        self.source = nums
        self.sums = []
        
        for i in range(0, len(nums)):
            self.sums.append(nums[i] if i == 0 else nums[i] + self.sums[i-1])

        print(self.source)
        print(self.sums)


    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]

        if left == right:
            return self.source[right]

        return self.sums[right] - self.sums[left] + self.source[left]


obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0, 2))
print(obj.sumRange(2, 5))
print(obj.sumRange(0, 5))


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)