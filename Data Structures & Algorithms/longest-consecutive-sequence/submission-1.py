class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        #just use sorting
        nums.sort()
        ans=1
        count=1
        for i in range(1,len(nums)):
            if(nums[i]==nums[i-1]):
                continue #ignore duplicates
            if(nums[i]-nums[i-1]==1):
                print(i,end=' ')
                count+=1
                continue
            ans=max(ans,count)
            count=1
        ans=max(ans,count) #very important line!
        return ans

            


            

        return 0
            
                   



        
        