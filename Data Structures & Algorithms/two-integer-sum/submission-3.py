class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dict to store memory
        prevMap = {}

        for i,n in enumerate(nums):
            # Calculate the complement
            diff = target - n
            # Check if complement in dict
            if diff in prevMap:
                #Return indices
                return [prevMap[diff], i]
            # Store number and indice
            prevMap[n] = i