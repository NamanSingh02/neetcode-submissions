import numpy as np
class Solution:
    def check(self,row:List[str])-> bool:
        valid=[]
        for num in row:
            if num<='9' and num>='0':
                valid.append(num)
            elif num!='.':
                return False

        num=set() #unordered set ->O(1) lookup and unique
        for i in valid:
            if i in num:
                return False
            else:
                num.add(i)
        return True
            
            
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board=np.array(board)
        #2D arrays can't be sliced if they are not numpy arrays
        #check all rows -> easiest!
        for i in range(9):
            ans=self.check(board[i])
            if ans==False:
                return False

        #check for columns
        for i in range(9):
            ans=self.check(board[:,i])
            if ans==False:
                return False

        #checking boxes ->Important
        for row in range(0,9,3):
            #starting row index
            for col in range(0,9,3):
                #starting column
                temp=board[row:row+3,col:col+3] #2 D matrix, shape=(3,3)
                temp=temp.flatten() #convert to vector
                ans=self.check(temp)
                #2D arrays can't be sliced if they are not numpy arrays
                if ans==False:
                    return False

        return True
        