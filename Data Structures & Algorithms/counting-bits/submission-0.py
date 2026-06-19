class Solution:
    def countBits(self, n: int) -> List[int]:
        result =[]

        for i in range(1 +n ):
            result.append(bin(i).count('1'))

        return result