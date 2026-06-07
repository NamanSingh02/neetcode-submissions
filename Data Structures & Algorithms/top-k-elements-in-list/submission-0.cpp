#include<algorithm>
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
        vector<pair<int,int>>v;
        for(auto x:freq){
            v.push_back(make_pair(x.second,x.first));
        }
        sort(v.rbegin(),v.rend());
        vector<int>res;
        for(int i=0;i<k;i++){
            res.push_back(v[i].second);
        }
        return res;
        
    }
};
