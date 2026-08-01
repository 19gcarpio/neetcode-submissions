class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #create dict
        freq = [[] for i in range(len(nums)+1)] #creating list of empty lists to put freq(index) by n in array

        for n in nums: 
            count[n] = 1+ count.get(n,0) # to get freq
        
        for n, cnt in count.items(): 
            freq[cnt].append(n) #put number in freq index
        
        res = []
        for i in range(len(freq) -1, 0, -1): #for every element in freq starting from last valid index before 0 counting backwards
            for n in freq[i]:  #for each number looking backwards store the n in the list to get most frequent to least
                res.append(n)
                if len(res) == k: #as soon as the length of the array equals K return the end list
                    return res

