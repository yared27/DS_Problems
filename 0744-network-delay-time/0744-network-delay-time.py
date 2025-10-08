class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}  
        for u, v, w in times:
            adj[u].append((v, w))

        pq = [(0, k)] 
        network = {i: float('inf') for i in range(1, n + 1)}
        network[k] = 0

        while pq:
            cur_time, cur = heapq.heappop(pq)

            for new_cur, weight in adj[cur]:
                new_time = cur_time + weight

                if new_time < network[new_cur]:
                    network[new_cur] = new_time
                    heapq.heappush(pq, (new_time, new_cur))

        max_time = max(network.values())
        return max_time if max_time != float('inf') else -1