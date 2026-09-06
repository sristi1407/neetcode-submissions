class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        max_odd = 0
        min_even = float('inf')

        for ch in s:
            freq[ch] = freq.get(ch,0) + 1 

        for count in freq.values():         
            if count % 2 == 1:              # odd frequency
                max_odd = max(max_odd, count)
            else:                          # even frequency
                min_even = min(min_even, count)

        return max_odd - min_even