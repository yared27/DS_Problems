class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        newList = [-num for num in stones]
        heapq.heapify(newList)
        while len(newList)>=2:
            x=-heapq.heappop(newList)
            y=-heapq.heappop(newList)

            if x!=y:
                y = abs(y-x)
                heapq.heappush(newList, -y)
            
        return -1*newList[0] if newList else 0