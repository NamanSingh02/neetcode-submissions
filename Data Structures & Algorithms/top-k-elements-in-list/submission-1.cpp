#include<algorithm>
#include<queue>
class Solution {
public:
    //set vs heaps
    //rbt vs heaps
    // Making O(NlogN), O(N)
    // extraction:
    //O(k), O(klogN)
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int>freq;
        for(int i=0;i<nums.size();i++){
            freq[nums[i]]++;
        }
        priority_queue<pair<int,int>>q;
        for(auto x: freq){
            q.push({x.second,x.first});
        }
        vector<int>ans;
        for(int i=0;i<k;i++){
            ans.push_back(q.top().second);
            q.pop();
        }
        return ans;
        
    }
};
