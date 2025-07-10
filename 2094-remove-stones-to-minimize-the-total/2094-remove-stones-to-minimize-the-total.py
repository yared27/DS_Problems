class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = [-num for num in piles]
        heapq.heapify(max_heap)
        for i in range(k):
            max_element = -heapq.heappop(max_heap)
            reduced = max_element - max_element//2
            heapq.heappush(max_heap,-reduced)
            
        return -sum(max_heap)