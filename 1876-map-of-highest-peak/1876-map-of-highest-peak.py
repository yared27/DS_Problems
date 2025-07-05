class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n , m = len(isWater), len(isWater[0])
        queue = deque()
        height_of_next_layer=1
        cell_heights = [[-1 for _ in range(m)] for _ in range(n)]

        for x in range(n):
            for y in range(m):
                if isWater[x][y] == 1:
                    queue.append((x, y))
                    cell_heights[x][y] = 0

        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m 
        while queue:
            # if (row,col) not in visited and inbound(row, col) and isWater[row][col] == 1:
            for _ in range(len(queue)):
                row,col = queue.popleft()
                for nr, nc in  [(0,1),(0,-1),(1,0),(-1,0)]:
                    newRow, newCol = row + nr, col + nc
                    if inbound(newRow,newCol) and cell_heights[newRow][newCol]==-1:
                            cell_heights[newRow][newCol]=height_of_next_layer
                            queue.append((newRow,newCol))
            height_of_next_layer+=1
            
        return cell_heights


                        



