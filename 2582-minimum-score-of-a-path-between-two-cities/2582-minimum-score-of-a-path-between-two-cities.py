class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, d in roads:
            graph[u].append((v,d))
            graph[v].append((u,d))
        res = float("inf")
        print(graph)
        def dfs(i):
            if i in visited:
                return
            nonlocal res
            visited.add(i)
            for neighbor, dist in graph[i]:
                res = min(res, dist)
                dfs(neighbor)
        visited = set()
        dfs(1)
        return res