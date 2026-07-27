class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        def hrs_needed(k):
            return sum(math.ceil(p/k) for p in piles)

        while left <= right :
            mid = (left+ right) // 2

            if hrs_needed(mid) <= h :
                right = mid -1 

            else :
                left = mid + 1

        return left  