class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower() #convert all characters to lower case
        i=0
        j=len(s)-1
        while(i<=j): #does it even make sense to proceed? 
            #make sure that s[i] is alphanumeric
            if (not s[i].isalnum()):
                i+=1
                continue
            if (not s[j].isalnum()):
                j-=1
                continue
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True

        