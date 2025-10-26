class Solution:
    def __init__(self):
        self.dir=[(1,0),(-1,0),(0,1),(0,-1)]
    def find(self,board,i,j,idx,word):
        if idx==len(word):
            return True
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or board[i][j]=='$': #outof bound or already visited
            return False 
        if board[i][j] != word[idx]: #not matched char
            return False

        #found the matched char now go for next
        temp=board[i][j]
        board[i][j]='$'
        for d in self.dir:
            i_ =i+ d[0]
            j_ =j+d[1]
            if self.find(board,i_,j_,idx+1,word):
                return True
        board[i][j]=temp
        return False
            

        
    def exist(self, board: list[list[str]], word: str) -> bool:
        m=len(board)
        n=len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0] and self.find(board,i,j,0,word):
                    return True
        return False

        