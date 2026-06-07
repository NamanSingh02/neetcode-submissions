class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==0:
            return False
        #s={} #set ->uses hashmaps similar to unordered_set
        s=set()
        #this is like a dictionary with no values!
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False

        