class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a hashset 
        hashset = set()

        # iterate through nums and check if in set
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        
        return False
        