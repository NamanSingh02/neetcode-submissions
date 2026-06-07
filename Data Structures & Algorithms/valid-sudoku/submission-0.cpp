class Solution {
public:
    
    bool check(vector<int>row){
        int arr[10]={0};
        for (int i:row){
            if(i=='.'){
                continue;
            }
            if(arr[i]!=0){
                return false;
            }
            arr[i]=1;
        }
        return true;
    }
    int find_box(int i,int j){
        if(i<3){
            if(j<3){
                return 0;
            }
            if(j<6){
                return 1;
            }
            if(j<9){
                return 2;
            }
        }
        if(i<6){
            if(j<3){
                return 3;
            }
            if(j<6){
                return 4;
            }
            if(j<9){
                return 5;
            }
        }
        if(i<9){
            if(j<3){
                return 6;
            }
            if(j<6){
                return 7;
            }
            if(j<9){
                return 8;
            }
        }
        return -1;
    }
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<vector<int>>row(9);//9 empty vectors ->tough in python
        vector<vector<int>>column(9);
        vector<vector<int>>box(9);

        for(int i=0;i<board.size();i++){
            for(int j=0;j<board.size();j++){
                if(board[i][j]=='.'){
                    continue;
                }
                int num=board[i][j]-'0';
                
                row[i].push_back(num);
                column[j].push_back(num);
                //find box
                box[find_box(i,j)].push_back(num);
            }
        }
        //check all!
        for(int i=0;i<9;i++){
            if(!(check(row[i]) and check(column[i]) and check(box[i]))){
                return false;
            }
        }
        return true;
        

        
    }
};
