class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)
        for i,eq in enumerate(equations):
            a,b = eq
            graph[a].append([b,values[i]])
            graph[b].append([a,1/values[i]])
        print(graph)
        def bfs(src,target):
            if src not in graph or target not in graph:
                return -1
            q,visit =deque(),set()
            q.append([src,1])
            visit.add(src)
            while q:
                n, w = q.popleft()
                if n == target:
                    return w
                for ni ,weight in graph[n]:
                    if ni not in visit:
                        q.append([ni,w*weight])
                        visit.add(ni)
            return -1
        return [bfs(q[0],q[1]) for q in queries]
