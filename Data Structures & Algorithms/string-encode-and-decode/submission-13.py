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
        sizes=""
        idx=-1
        for ch in s:
            idx+=1
            if ch=='#':
                break
            sizes+=ch
        if sizes=="":
            return []
        
        #now sizes="1,0,2,"
        sizes=sizes.split(',')
        sizes=[int(st) for st in sizes]
        #sizes is now list[int]
        j=0 #first integer
        s=s[idx+1:] #only consider relevant part

        ans=[]
        for i in sizes:
            #extract i characters from s
            ans.append(s[:i])
            s=s[i:] #remove first i characters
        return ans






            

