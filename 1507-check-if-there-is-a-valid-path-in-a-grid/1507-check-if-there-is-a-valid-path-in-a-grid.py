class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        directions = {
            1:[(0,1),(0,-1)],
            2:[(-1,0),(1,0)],
            3:[(0,-1),(1,0)],
            4:[(0,1),(1,0)],
            5:[(0,-1),(-1,0)],
            6:[(0,1),(-1,0)]

        }

        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        destination=(len(grid)-1,len(grid[0])-1)
        def inbound(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])

        def dfs(row,col):
            visited[row][col]=True
            if (row,col)==destination:
                return True
            for dr,dc in directions[grid[row][col]]:
                nc=col+dc
                nr=row+dr
                if inbound(nr,nc) and not visited[nr][nc] and (-dr,-dc) in directions[grid[nr][nc]]:
                    if dfs(nr,nc):
                        return True
            return False
        return dfs(0,0)