class Solution(object):
    def constructProductMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        MOD = 12345
        m = len(grid)
        n = len(grid[0])
        ans = [[0] * n for _ in range(m)]
        prefix = [1]
        suffix = 1

        for row in grid:
            for num in row:
                prefix.append(prefix[-1] * num % MOD)

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                ans[i][j] = prefix[i * n + j] * suffix % MOD
                suffix = suffix * grid[i][j] % MOD

        return ans
