class Solution {
public:
    int maxArea(vector<int>& h) {
        int i=0;
        int j=h.size()-1;
        int ans=0;

        while(i<j){
            int area=(j-i)*min(h[j],h[i]);
            ans=max(ans,area);
            if (h[j]<h[i]){
                j--;
            }
            else if (h[i]<h[j]){
                i++;
            }
            else{
                j--;
                i++;
            }
        }
        return ans;
    }
};
