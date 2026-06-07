class Solution {
public:
    bool test(string s, int i){
        if(s.size()-i >=5){
            string s2;
            for(int j=0;j<5;j++){
                s2+=s[i];
                i++;
            }
            if(s2=="naman"){
                return true;
            }
        }
        return false;
    }
    string encode(vector<string>& strs) {
        string s;
        for(int i=0;i<strs.size();i++){
            s+=strs[i];
            s+="naman"; //delimitor
        }
        return s;
    }
    vector<string> decode(string s) {
        vector<string>v;
        string s2;
        for(int i=0;i<s.size();i++){
            if(s[i]!='n'){
                s2+=s[i];
                continue;
            }
            if(test(s,i)){
                i+=4;
                v.push_back(s2);
                s2="";
                continue;
            }
            s2+=s[i];
        }
        return v;
    }
};
