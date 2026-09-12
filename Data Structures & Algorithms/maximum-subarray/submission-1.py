class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum =nums[0]
        max_sum = nums[0]
        for num in range(1,len(nums)):
            current_sum = max(nums[num],current_sum+nums[num])
            max_sum = max(current_sum,max_sum)

        return max_sum
