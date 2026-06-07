class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we wanna solve it this time without / as required
        #idea: ans[i]=left*right
        #to find them we will need 2 passes as well
        dict={};
        dict[0]=[1,None]
        dict[len(nums)-1]=[None,1]
        for i in range(1,len(nums)):
            if (i!=len(nums)-1):
                dict[i]=[None,None]
            dict[i][0]=dict[i-1][0]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            dict[i][1]=dict[i+1][1]*nums[i+1]
        ans=[]
        for i in range(len(nums)):
            ans.append(dict[i][0]*dict[i][1])
        return ans

            
        
        