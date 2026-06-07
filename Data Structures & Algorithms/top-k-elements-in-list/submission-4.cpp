#include<algorithm>
#include<queue>
class Solution {
public:
    //Final cheating way!
    //only applicable when sizes are small
    //We use direct addressing.
    //should we plot frequencies or the numbers?
    //frequencies!! because we will be able to extract them k largest 
    //Bucket Sort -> grouping integers of same frequencies together
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int>freq;
        for(int i=0;i<nums.size();i++){
            freq[nums[i]]++;
        }
        unordered_map<int,vector<int>>groups;// we can use arrays too
        for(auto x:freq){
            groups[x.second].push_back(x.first);
        }
        vector<int>ans;
        for(int i=nums.size();i>=0;i--){
            //max frequency may be nums.size()
            if(groups[i].empty()) continue;
            for(int j=0;j<groups[i].size();j++){
                //note: in python regular arrays(not numpy)
                //we can directly write ans+=groups[i]
                //but in that case size may exceed k
                ans.push_back(groups[i][j]);
                if(ans.size()==k){
                    return ans;
                }
            }
        }
        return ans;
        
    }
};
