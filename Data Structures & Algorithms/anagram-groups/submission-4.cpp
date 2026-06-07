class Solution {
public:
    string char_freq(string s){
        vector<int>freq(26,0);
        for(char ch: s){
            freq[ch-'a']++;
        }
        //The real question: how do we make this vector hashable?
        //convert to strings!! ->similar to tuple in Python
        if (s.size()==0){
            return "()"; //empty tuple string
        }
        string ans="(";
        for(int i=0;i<freq.size()-1;i++){
            string num=to_string(freq[i]);
            //ans.push_back(num); ->push_back can only add 1 character!
            ans+=num;
            ans.push_back(',');
        }
        string num=to_string(freq[freq.size()-1]);
        ans+=num;
        ans.push_back(')');
        return ans;

    }
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>>groups;
        for (string s:strs){
            string freq=char_freq(s);
            groups[freq].push_back(s);
        }
        vector<vector<string>>ans;
        for(auto group:groups){
            ans.push_back(group.second);
        }
        return ans;
        //time=O(mn)
        //space=O(mn)
        
    }
};
