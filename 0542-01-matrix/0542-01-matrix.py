class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n , m = len(mat), len(mat[0])
        nearestZero = [[-1 for _ in range(m)]for _ in range(n)]
        queue = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    nearestZero[i][j] = 0
                    queue.append([i,j])
        while queue:
                x,y = queue.popleft()
                for nr , nc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    newRow, newCol = x+nr, y+nc
                    if 0<= newRow < n and 0<= newCol < m and nearestZero[newRow][newCol]==-1:
                            nearestZero[newRow][newCol] = nearestZero[x][y]+1
                            queue.append([newRow, newCol])

        return nearestZero