import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #step 1: calculate their frequency
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        #step 2: use max-heap, key=freq
        max_heap=[(-j,i) for i,j in freq.items()] #for heaps we cannot select the 2nd element as the key, it is not like sort
        #i=number, j=freq
        heapq.heapify(max_heap)
        ans=[]
        print(max_heap)
        for _ in range(k):
            freq, num=heapq.heappop(max_heap)
            freq=-freq #unnecessary!
            ans.append(num)
        return ans



        
