class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l=0
        r=len(nums) -1 
        res=0
        MOD=10**9 +7
        power=[1]*len(nums)

        for i in range (1,len(nums)):
            power[i]=(power[i-1]*2)%MOD


        while l<=r:
            if nums[l] + nums[r] <= target :
                res=(res+power[r-l]) % MOD

                l=l+1

            else:
                r=r-1

        return res

