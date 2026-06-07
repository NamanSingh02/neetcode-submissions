class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}

        for i,num in enumerate(nums):
            need=target-num
            # seen[num]=i -> No!! update later!
            if need not in seen:
                seen[num]=i
                continue
            return [seen[need],i]
            
            
        