class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        fresh = 0
        q =collections.deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        if fresh==0:
            return 0
        minutes =-1
        while q:
            for _ in range(len(q)):
                row,col = q.popleft()
                for nr,nc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nrow = nr+row
                    ncol = nc+col
                    if 0<=nrow<n and 0<=ncol<m and grid[nrow][ncol]==1:
                        grid[nrow][ncol]=2
                        q.append((nrow,ncol))
                        fresh-=1
            minutes+=1
        return minutes if fresh==0 else -1            

