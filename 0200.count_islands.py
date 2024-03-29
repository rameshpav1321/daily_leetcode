# bfs based solution
from queue import Queue
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        visited=set()
        def bfs(row,col):
            q=Queue()
            visited.add((row,col))
            q.put((row,col))
            while q.empty()==False:
                curr_row,curr_col=q.get()
                possible_movements=[[1,0],[-1,0],[0,1],[0,-1]]
                for r_step,c_step in possible_movements:
                    new_row,new_col=curr_row+r_step,curr_col+c_step
                    if (new_row in range(rows)) and (new_col in range(cols)) and grid[new_row][new_col]=="1" and (new_row,new_col) not in visited:
                        q.put((new_row,new_col))
                        visited.add((new_row,new_col))
        count=0
        rows,cols=len(grid),len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1" and (i,j) not in visited:
                    count+=1
                    bfs(i,j)
        return count

# dfs based solution
class Solution:
    def dfs(self,grid,row,col,rows,cols):
        if row<0 or row>=rows or col<0 or col>=cols:
            return
        if grid[row][col]!='1':
            return
        grid[row][col]='v'
        self.dfs(grid,row-1,col,rows,cols)
        self.dfs(grid,row+1,col,rows,cols)
        self.dfs(grid,row,col-1,rows,cols)
        self.dfs(grid,row,col+1,rows,cols)

    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        rows,cols=len(grid),len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    self.dfs(grid,i,j,rows,cols)
                    count+=1
        return count