class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        def dfs(r, c):
            if not inbound(r, c) or grid[r][c] != '1':
                return
            grid[r][c] = '0' 
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(r + dr, c + dc)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count
