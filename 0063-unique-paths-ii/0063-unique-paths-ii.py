class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)]

        if obstacleGrid[n-1][m-1] == 0:
            dp[n-1][m-1] = 1

        def uniquePath(i, j):
            if i<n and j<m and obstacleGrid[i][j] !=1:
                return dp[i][j]
            return 0

        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if obstacleGrid[i][j]!=1:
                    if not (i==n-1 and j==m-1):
                        dp[i][j] = uniquePath(i+1,j) + uniquePath(i,j+1)
                    
        return dp[0][0]