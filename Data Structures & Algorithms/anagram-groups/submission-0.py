class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            sorS =''.join(sorted(s))
            res[sorS].append(s)
        return list(res.values())


        

        