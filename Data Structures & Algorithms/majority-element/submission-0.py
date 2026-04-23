class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res=0
        count =0 
        for num in nums:
            if count ==0:
                res=num
            if num==res:
                count=count+1
            else:
                count=count-1
        return res



         
                

        