class Solution:
    #universal solution: Same idea as 2, but shorter solution -> Python style :)
    def encode(self, strs: List[str]) -> str:
        sizes:str=""
        strings:str=""
        lengths=[str(len(s)) for s in strs]
        sizes=','.join(lengths) + '#'
        strings="".join(strs)
        #acts like a delimitor -> 
        #read until the first # is found
        #can't we use , ? ->No! 
        #last comma may be in the strings as well

        sizes+=strings
        return sizes



    def decode(self, s: str) -> List[str]:
        sizes, s = s.split("#",1) #max splits is 1 -> split from first #
        
        #now sizes="1,0,2"
        if sizes=="":
            return []

        sizes=sizes.split(',') #["1","0","2"]

        sizes=[int(st) for st in sizes]
        #sizes is now list[int]

        ans=[]
        idx=0
        for i in sizes:
            #extract i characters from s
            ans.append(s[idx:idx+i])
            idx+=i #remove first i characters
        return ans






            

