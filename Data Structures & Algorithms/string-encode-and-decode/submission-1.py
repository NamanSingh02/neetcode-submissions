class Solution:

    def encode(self, strs: List[str]) -> str:
        #we will just combine all the strings with a delimitor 'naman'
        ans=""
        for s in strs:
            ans+=s
            ans+="naman"
        return ans

    def decode(self, s: str) -> List[str]:
        #split the string across 'naman'
        ans=s.split("naman")
        #we have an empty string in the end
        ans.pop()
        return ans
