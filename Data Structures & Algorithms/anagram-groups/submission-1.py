class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #string to character frequency hashmap (table)
        str_ch={}
        #step 1: making str -> char frequency table
        #time = O(mn)
        for s in strs:
            if s in str_ch:
                continue
            str_ch[s]={} #The value for this key is also a hashmap
            for ch in s:
                if ch in str_ch[s]:
                    str_ch[s][ch]+=1
                else:
                    str_ch[s][ch]=1
        groups={}
        #step 2: Form groups
        #groups: group_leader ->list of members
        #worst case, time = O(m^2)
        for s in strs:
            if s in groups:
                groups[s].append(s)
                continue
            for s_lead in groups:
                if str_ch[s_lead]==str_ch[s]:
                    #same group
                    groups[s_lead].append(s)
                    break
            else: #form a new group
                groups[s]=[s]
        #return groups, worst case = O(m)
        ans=[]
        #for leader, group in groups: ->doesn't work!
        for leader in groups:
            ans.append(groups[leader])
        return ans
                
        


        