class Solution:
    def twosum(self, nums:List[int], i,target) -> List[List[int]]:
        start=i
        j=len(nums)-1
        l=[] #elements should be unique pairs!
        while i<j:
            s=nums[i]+nums[j]
            if s==target:
                l.append([nums[i],nums[j]])
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
        ans=set()
        for i in range(len(nums)-2):
            a=nums[i] #a will be our smallest element
            if a>0: 
                break #the smallest number can't be +ve

            l=self.twosum(nums,i+1,-a)
            if len(l)==0: #unnecessary
                continue
            for l2 in l:
                ans.add(tuple([a]+l2))
        #convert set of tuples to list of lists
        ans=[list(l) for l in ans]
        return ans
            






        