class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True
        decreasing = True
        n = len(nums)
        for i in range(1,n) :
            if (nums[i] < nums[i-1]):
                increasing = False

            if (nums[i] > nums[i-1]):
                decreasing = False

        return increasing or decreasing
