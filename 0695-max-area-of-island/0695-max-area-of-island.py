class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        maximumArea = 0
        def unbound(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])
        visited = set()
        def dfs(row,col,visited):
            visited.add((row,col))
            area=1
            for dr,dc in directions:
                new_row=row+dr
                new_col=col+dc
                if unbound(new_row,new_col) and (new_row,new_col) not in visited and grid[new_row][new_col]==1:
                    area+=dfs(new_row,new_col,visited)
            return area
        for i in range(len(grid)):     
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                   maximumArea=max(maximumArea,dfs(i,j,visited))
        return maximumArea





