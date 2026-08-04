class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a default dict
        res = defaultdict(list)
        # Create key of sorted S then append anagrams
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
