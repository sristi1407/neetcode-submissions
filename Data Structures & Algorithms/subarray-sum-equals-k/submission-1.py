class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        currsum = 0

        prefix_sum ={0:1}

        for num in nums :
            currsum = currsum + num

            if currsum - k in prefix_sum :
                res = res + prefix_sum[currsum - k ]

            prefix_sum[currsum]= prefix_sum.get(currsum, 0) + 1 

        return res
