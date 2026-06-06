class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        frequency = {}

        for num in nums :
            frequency[num]=frequency.get(num,0)+1

        for num in frequency:
            if frequency[num]> len(nums) // 2:
                return num

       # return num 

        

         
                

        