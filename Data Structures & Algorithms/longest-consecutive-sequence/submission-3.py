class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Brute force: every element can be start
        #method 2: sorting -> as order is irrelevant
        if len(nums)==0:
            return 0
        #use unordered set
        hash_set=set(nums)#put all elements
        ans=1
        for start in nums: #in python, start won't be affected by inside increments
            #is start even possible?
            if (start-1) in hash_set:
                continue #nope ->Can never be a start
                #start-1 ko start banao na!
            #we have an eligible start value
            #Now use brute force!!
            count=1
            start+=1 #next element dhundo
            while start in hash_set:
                #while loop doesn't really depend on N, and it only runs as long as we can continue to find consecutive elements
                #for most elements it won't even run once
                count+=1
                start+=1
            #we couldn't find start+1
            ans=max(ans,count)
        return ans
            
                   



        
        