#m=no. of strings
#n=size of longest string
class Solution:
    def char_freq(self, s: str)->tuple:
        #it is given that letters are only a to z (26)
        freq=[0]*26
        for ch in s:
            idx=ord(ch)-ord('a')
            freq[idx]+=1
        return tuple(freq)
        #NOTE: Tuples are immutable and are directly hashable in Python

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        for s in strs:
            freq=self.char_freq(s)
            if freq in groups:
                groups[freq].append(s)
            else:
                groups[freq]=[s]
        #time=O(mn)
        #space=O(mn) ->key size is fixed but the group of anagrams still depend on n
        return list(groups.values())
            



        