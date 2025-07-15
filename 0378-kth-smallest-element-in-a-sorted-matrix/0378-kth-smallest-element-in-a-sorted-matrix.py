class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        newlist = []
        for j in range(len(matrix)):
            newlist+=matrix[j]
        newlist.sort()
        return newlist[k-1]       