class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        seen = set(nums)
        n=len(nums)

        for num in range(1,n+1):
            if num not in seen:
                res.append(num)

        return res 
