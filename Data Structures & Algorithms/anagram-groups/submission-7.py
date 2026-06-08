#m=no. of strings
#n=size of longest string
class Solution:
    def char_freq(self, s: str)->Dict:
        freq={}
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=0
        #Why are hashmaps/dictionaries not hashable? because they are mutable and can be edited in place
        #So we need to make them constant/freeze them/make them immutable
        return frozenset(freq.items()) #like set of tuples of key-value pairs
        #Not exactly a STL set
        #what if we don't write values()? ->frozen set will only include keys!

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
            



        