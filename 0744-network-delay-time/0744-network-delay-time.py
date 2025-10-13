class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i:[] for i in range(1,n+1)}

        for u, v, w in times:
            graph[u].append((v,w))
        times = [float('inf')]*(n+1)
        times[k] = 0
        heap = [(times[k],k)]

        while heap:
            w, node = heapq.heappop(heap)
            if w > times[node]:
                continue
            for n, wt in graph[node]:
                if wt+w < times[n]:
                    times[n] = wt+w
                    heapq.heappush(heap, (times[n], n))
        return max(times[1:]) if max(times[1:]) != float("inf") else -1
