class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        minHeap = []

        for i in range(n):
            heapq.heappush(minHeap, (matrix[i][0],i,0))

        count = 0

        while minHeap:
            count+=1
            val, r, c = heapq.heappop(minHeap)
            if count == k:
                return val
            if c+1<n:
                heapq.heappush(minHeap, (matrix[r][c+1],r,c+1))
        