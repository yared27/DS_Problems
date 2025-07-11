class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = Counter(nums)
        
        numList = list(set((numMap.values())))
        freqMap = defaultdict(list)
        for key, val in numMap.items():
            freqMap[val].append(key)

        numList = [-n for n in numList]

        heapq.heapify(numList)


        result = []

        while k > 0:
            freq = -heapq.heappop(numList)
            for num in freqMap[freq]:
                result.append(num)
                k -= 1
                if k == 0:
                    break
        return result