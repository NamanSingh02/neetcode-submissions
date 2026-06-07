class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={} #map: num -> list(indices)
        for i in range(len(nums)):
            num=nums[i]
            if num in map:
                map[num].append(i)
            else:
                map[num]=[i]
        for i in range(len(nums)):
            num=nums[i]
            #do we have target-num?
            if target-num not in map:
                continue
            #we have it
            l=map[target-num]
            #we are given that we have a unique pair
            for j in l:
                if j!=i:
                    return [i,j]




        