class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        
        if obstacleGrid[m-1][n-1] == 0:
            dp[m-1][n-1] = 1
        
        def uniquePath(i, j):
            if i < m and j < n and obstacleGrid[i][j] != 1:
                return dp[i][j]
            return 0
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if obstacleGrid[i][j] != 1:
                    if not (i == m-1 and j == n-1):  # skip base case cell
                        dp[i][j] = uniquePath(i+1, j) + uniquePath(i, j+1)
        
        return dp[0][0]
