class Solution:
    def twosum(self, nums:List[int], i,target) -> List[List[int]]:
        start=i
        j=len(nums)-1
        l=[] #elements should be unique pairs!
        while i<j:
            if i!=start and nums[i]==nums[i-1]:
                #we can't look behind start
                #already done!
                i+=1
                continue
            if j!=len(nums)-1 and nums[j]==nums[j+1]:
                j-=1 # technically this condition is unnecessary
                continue # But one often thinks it because it is intuitive and doesn't make the solution wrong
            s=nums[i]+nums[j]
            if s==target:
                l.append([nums[i],nums[j]])
                #we gotta skip repeated i and j
                i+=1
                j-=1
                #if any remains same, the possible answer will be a duplicate
            elif s<target:
                i+=1
            else:
                j-=1
        return l


    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we need to compare with a value -> sorting is always convenient
        # also the indices are not important
        #we need to remove duplicates which will be easy because the elements will be sorted
        nums.sort()

        #fix 1 number and use 2 pointer on the others
        ans=[]
        for i in range(len(nums)):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            a=nums[i]
            if a>0: 
                break #the smallest number can't be +ve

            l=self.twosum(nums,i+1,-a)
            if len(l)==0:
                continue
            for l2 in l:
                ans.append([a]+l2)
        return ans
            






        