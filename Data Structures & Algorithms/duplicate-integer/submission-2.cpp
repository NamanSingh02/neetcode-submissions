#include<unordered_set>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        if(nums.size()==0){
            return 0;
        }
        unordered_set<int>s;
        for(int i=0;i<nums.size();i++){
            if(s.count(nums[i])){
                return 1;
            }
            s.insert(nums[i]);
        }
        return 0;
    }
};