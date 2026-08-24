class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #1 Create a hashset to check if value in hashmap and if not add to iterate through the list
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False