class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #problem arises in case of 0s, product=0 and 0/0 is indeterminate
        product_actual=1
        product=1
        freq=0 #frequency of 0s
        for num in nums:
            if num==0:
                freq+=1
                product_actual=0
                continue
            product*=num
            product_actual*=num
        ans=[0]*len(nums)
        if freq>=2:
            return ans
        
        for i in range(len(ans)):
            if nums[i]!=0:
                ans[i]=int(product_actual/nums[i])
            else:
                ans[i]=int(product)
        return ans


        