from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=''
        for s in strs:
            ans+=s
            ans+="naman"
        return ans


    def decode(self, s: str) -> List[str]:
        ans=s.split("naman")
        ans.pop()
        return ans