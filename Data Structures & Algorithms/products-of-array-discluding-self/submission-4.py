#we use prefix product and suffix product
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we wanna solve it this time without / as required
        #idea: ans[i]=left*right
        #to find them we will need 2 passes as well
        n=len(nums)
        left=[0]*n
        right=[0]*n
        left[0]=right[n-1]=1
        for i in range(1,n):
            #left creation
            left[i]=left[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            #right creation
            right[i]=right[i+1]*nums[i+1]
        ans=[0]*n
        for i in range(n):
            ans[i]=left[i]*right[i]
        return ans


            
        
        