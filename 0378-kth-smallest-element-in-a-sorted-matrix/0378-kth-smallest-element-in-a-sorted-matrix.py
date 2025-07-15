class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        newlist = []
        for j in range(len(matrix)):
            newlist+=matrix[j]
        heapq.heapify(newlist)
        minElemnt = 0 
        for i in range(k):
            minElemnt = heapq.heappop(newlist)
        return minElemnt