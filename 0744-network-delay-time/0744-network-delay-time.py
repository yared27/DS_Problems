class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i:[] for i in range(1,n+1)}

        for u, v, t in times:
            graph[u].append((v,t))

        distances = [float("inf")]*(n+1)
        distances[k] = 0
        hp = [(0,k)]

        while hp:
            time, node = heapq.heappop(hp)
            if time > distances[node]:
                continue 
            for child, childTime in graph[node]:
                new_time = childTime + time
                if distances[child] > new_time:
                    distances[child] = new_time
                    heapq.heappush(hp,(new_time, child))

        return max(distances[1:]) if max(distances[1:]) != float("inf") else -1