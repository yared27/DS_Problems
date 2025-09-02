class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        root = {i : i for i in range(1,n+1)}
        rank = [0]*(n+1)

        def find(x):
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            return root[x]
        
        def union(x, y):
            yroot = find(y)
            xroot = find(x)

            if yroot != xroot:
                if rank[yroot] > rank[xroot]:
                    root[xroot] = yroot
                elif rank[xroot] > rank[yroot]:
                    root[yroot] = xroot
                else:
                    root[yroot] = xroot
                    rank[xroot] += 1
        for node in edges:
            x, y = node
            if find(x) != find(y):
                union(x, y)
            else:
                return node                