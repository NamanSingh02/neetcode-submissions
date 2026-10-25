class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        //Binary search -> O(NlogN)
        //Hashmaps -> time = O(N) space = O(N)
        //2 points : O(N) space O(1)

        // Indicators: sorted array -> can be easily manipulated, comparison with a target

        int i=0;
        int j=numbers.size()-1;
        vector<int>v;
        while(i<j){
            int s=numbers[i]+numbers[j];
            if(s==target){
                v.push_back(i+1);
                v.push_back(j+1);
                return v;
            }
            else if (s<target){
                //sum must be increased
                i++;
            }
            else{
                j--;
            }
        }

    }
};
