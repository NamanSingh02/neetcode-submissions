//Motivation: Anything is possible
//Bas Bande mei dam hona chahiye!

//What are we going to do?

//we will make the char_freq hashmap as our key!!! 
/*
size_t=size_t is the standard return type used by C++ hash functions. (non-negative integer-like value)


we are overloading the function call operator.
hashf h;
unordered_map<char,int> freq;

h(freq);   // this calls operator()(freq)

So this:
h(freq)
is secretly:
h.operator()(freq)


We use reference & so that the whole hashmap is not copied.


const map ->hashing should not change the key!


const{ ->The hash function itself will not modify the hashf object!
}
*/

// --------------------------------------------------------------------

class hashf{
    public:
    size_t operator()(const unordered_map<char,int>& char_freq)const{
        int hash_value=0;
        for(auto x:char_freq){
            hash_value-=int(x.first);
            hash_value+=(x.second);
        }
        return hash_value;
    }
};
class Solution {
public:
    unordered_map<char,int> char_freq(string s){
        unordered_map<char,int>freq;
        for(char ch: s){
            freq[ch]++;
        }
        return freq;
    }
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<unordered_map<char,int>,vector<string>, hashf>groups;
        for (string s:strs){
            unordered_map<char,int> freq=char_freq(s);
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
