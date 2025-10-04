class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        print(heights)
        hp = [(0,0,0)]
        COL = len(heights[0])
        ROW = len(heights)
        effort = [[float("inf")]*COL for _ in range(ROW)]
        effort[0][0] = 0
        print(effort)
        directions = [(1,0),(-1,0),(0,-1),(0,1)]
        while hp:
            w, row, col = heappop(hp)
            if row == ROW-1 and col == COL-1:
                return w
            for nr, nc in directions:
                newRow = row + nr
                newCol = col + nc
                if 0 <= newRow < ROW and 0 <= newCol and newCol < COL:
                    newEffort = max(w, abs(heights[newRow][newCol] - heights[row][col]))
                    if newEffort < effort[newRow][newCol]:
                        effort[newRow][newCol] = newEffort
                        heapq.heappush(hp, (newEffort, newRow, newCol))

        return -1
