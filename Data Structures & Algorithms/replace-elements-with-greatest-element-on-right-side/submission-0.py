class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = -1

        for i in range(len(arr) -1 ,-1,-1):
            temp = arr[i]
            arr[i] = result
            result= max(result,temp)
        return arr

