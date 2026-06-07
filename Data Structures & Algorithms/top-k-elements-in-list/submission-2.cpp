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
        
        vector<pair<int,int>>temp;

        for(auto x: freq){
            temp.push_back({x.second,x.first});
        }
        priority_queue<pair<int,int>>q(temp.begin(),temp.end());
        vector<int>ans;
        for(int i=0;i<k;i++){
            ans.push_back(q.top().second);
            q.pop();
        }
        return ans;
        
    }
};
