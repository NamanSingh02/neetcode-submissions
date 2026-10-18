#best
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower() #convert all characters to lower case
        l=[ch for ch in s if ch.isalnum()]
        #extra O(N) space wastage
        s="".join(l)
        i=0
        j=len(s)-1
        while(i<=j): #does it even make sense to proceed? 
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True

        