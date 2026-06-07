class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        unordered_set<int>s; //0 indices!
        //hashmaps we can search for an index in O(1) time, though it was not necessary :(
        int prod=1;
        for(int i=0;i<nums.size();i++){
            if(nums[i]==0){
                s.insert(i);
                continue;
            }
            prod*=nums[i];
        }
        vector<int>ans(nums.size());
        for(int i=0;i<nums.size();i++){
            if(s.size()!=0){
                //there are 0s
                if(nums[i]!=0){
                    ans[i]=0;
                }
                else{//nums[i]=0
                    if(s.size()>1){
                        ans[i]=0;//iske ilawa bhi 0s hai
                    }
                    else{
                        ans[i]=prod;
                    }
                }
            }
            else{
                // we don't have 0s
                ans[i]=prod/nums[i];
            }

        }
        return ans;
    }
};
