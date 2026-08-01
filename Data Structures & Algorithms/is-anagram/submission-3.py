class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # First check if len is the same
        if len(s) != len(t):
            return False
        # Create dict to count letters to create comparison
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
            countT[t[i]] = 1 + countT.get(t[i],0)
        # Check if anagram
        return countS == countT