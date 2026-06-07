class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups={}
        #time=O(mnlogn)
        for s in strs:
            sorted_s=''.join(sorted(s)) #O(nlogn)
            if sorted_s in groups:
                groups[sorted_s].append(s)
            else:
                groups[sorted_s]=[s]
        #return list of all values in dictionary
        return list(groups.values()) 
        


        