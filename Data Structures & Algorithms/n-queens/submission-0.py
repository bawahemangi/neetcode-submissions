class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        posdia=set()
        negdia=set()
        board=[['.']*n for _ in range(n)]
        res=[]

        def dfs(r):
            if r==n:
                copy=[''.join(row) for row in board]

                res.append(copy)
                return 

            for c in range(n):
                if (c in col or (r-c ) in negdia or (r+c) in posdia):
                    continue
                col.add(c)
                posdia.add(r+c)
                negdia.add(r-c)
                board[r][c]='Q'

                dfs(r+1)
                
                col.remove(c)
                posdia.remove(r+c)
                negdia.remove(r-c)
                board[r][c]='.'

        dfs(0)
        return res