class Solution:

    def encode(self, strs: List[str]) -> str:
        res = '' # start with empty string to build encoded result
        for s in strs: # loop through each string in the input list
            res += str(len(s)) + "#" + s # add: <length> + "#" + <string>
        return res # return the whole encoded string
   
    def decode(self, s: str) -> List[str]:
        res = [] #list to collect decoded strings
        i = 0 #pointer into the big encoded string

        while i < len(s): # keep going until we've parsed the entire string
            j = i #start another pointer at the same spot
            while s[j] != "#": # move j forward until we hit the '#' separator
                j += 1 
            length = int(s[i:j]) #substring from i up to j are the didgts for length
            i = j + 1 #move i to the first character of the string content
            j = i + length #calculate where the string ends using the length
            res.append(s[i:j]) # slice the encoded string and append to list
            i = j #move i to the end of the word/phrase we decoded and loop again
        return res # return all decoded strings


        