class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        w=0
        r=1

        for r in range(1,len(nums)):
            if nums[w] != nums[r]:
                w=w+1
                nums[w]=nums[r]
            else:
                r=r+1

            

        return w +1 

        
        