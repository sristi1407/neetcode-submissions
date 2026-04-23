class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        num =set(nums)
        for i in num:
            if (i-1) not in num :
                length =1 
                while (i + length) in num:
                    length += 1
                
                res= max(length,res)
        return res