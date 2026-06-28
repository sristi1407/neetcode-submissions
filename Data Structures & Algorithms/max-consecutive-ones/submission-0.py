class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        current = 0
        max_so_far=0

        for num in nums:

            if num == 1 :
                current +=1
                max_so_far = max(current,max_so_far)

            else :
                current = 0

        return max_so_far

