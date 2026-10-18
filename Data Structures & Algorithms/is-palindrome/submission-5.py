class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower() #convert all characters to lower case
        i=0
        j=len(s)-1
        while(i<=j):
            #problem: what if last i and j are both not alphanumeric?
            #correct answer should be true
            #make sure that s[i] is alphanumeric
            while(not s[i].isalnum()):
                i+=1
                if i>j:
                    return True #not false
                    #we overshoot j that means j se pehle koi alnum nahi bacha hai
            while(not s[j].isalnum()):
                j-=1
                if j<i:
                    return True
            if s[i]!=s[j]:
                print("end")
                return False
            i+=1
            j-=1
        return True

        