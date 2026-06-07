class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        #use unordered set
        hash_set=set(nums)#put all elements
        ans=1
        for start in nums:
            count=1
            start+=1
            while start in hash_set:
                count+=1
                start+=1
            ans=max(ans,count)
        return ans
            
                   



        
        