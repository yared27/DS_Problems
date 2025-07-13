class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        newList = [-num for num in nums]
        heapq.heapify(newList)
        ans = 0
        for i in range(k):
            ans = heapq.heappop(newList) 
        return -1*ans