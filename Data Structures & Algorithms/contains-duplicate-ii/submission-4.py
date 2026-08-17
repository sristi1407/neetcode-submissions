class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
    

        for num in range(len(nums)):
            if nums[num] in seen :
                if num - seen[nums[num]] <= k:
                    return True
            

            seen[nums[num]] = num
        return False