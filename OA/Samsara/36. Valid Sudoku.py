class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        r=[[0 for _ in range(9)] for _ in range(9)]
        c=[[0 for _ in range(9)]for _ in range(9)]
        m=[[[0 for _ in range(9)] for _ in range(3)] for _ in range(3)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    
                    temp=int(board[i][j])-1
                    if r[i][temp] or c[j][temp] or m[i//3][j//3][temp]:
                      
                        return False
                    else:
                        print(i,temp)
                        r[i][temp]=1
                        c[j][temp]=1
                        m[i//3][j//3][temp]=1
                     
        return True
        