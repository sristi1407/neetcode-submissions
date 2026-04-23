class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)

        for words in strs:
            count =[0] * 26

            for ch in words:
                count[ord(ch)-ord('a')] += 1

            result[tuple(count)].append(words)
        return list(result.values())