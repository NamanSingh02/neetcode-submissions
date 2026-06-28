class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #step 1: calculate their frequency
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        #thought ->what if we add them to a max heap based on frequency?
        #we could!
        #step 2: Plot frequency -> numbers
        print(freq)
        groups={}
        #for ele,f in enumerate(freq.items()): enumerate gives indices of each element received
        for ele,f in freq.items():
            if f in groups:
                groups[f].append(ele)
            else:
                groups[f]=[ele]
        print(groups)
        ans=[]
        for size in range (len(nums),-1,-1):
            #max freq could be len(nums)
            if size in groups:
                ans=ans+groups[size]
                if len(ans)==k:
                    break
        return ans




        