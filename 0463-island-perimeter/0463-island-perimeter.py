class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        def inbound(row,col):
            return (0<=row<=len(grid) and 0<=col<=len(grid[0]))
        visited=[[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def inbound(row,col):
            return (0<=row<len(grid) and 0<=col<len(grid[0]))
        perimeter=0
        def dfs(row,col,visited):
            nonlocal perimeter
            visited[row][col]=True
            for dr,dc in direction:
                    new_row=row+dr
                    new_col=col+dc
                    if not inbound(new_row,new_col) or grid[new_row][new_col]==0:
                             perimeter+=1
                    elif not visited[new_row][new_col] and grid[new_row][new_col]==1:
                         dfs(new_row,new_col,visited)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]==1:
                    dfs(row,col,visited)
                    return perimeter
        return 0

            


