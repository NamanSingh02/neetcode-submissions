class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #approach 3: min heap!
        #the min heap would store the k largest frequencies
        #step 1: calculate their frequency
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        min_heap=[]
        for num,count in freq.items():
            heapq.heappush(min_heap, (count, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        ans=[num for (count, num) in min_heap]
        return ans


        
        