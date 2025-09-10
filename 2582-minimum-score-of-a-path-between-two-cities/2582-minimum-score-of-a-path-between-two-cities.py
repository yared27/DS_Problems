class UnionFind:
    def __init__(self, n):
        self.root = {i: i for i in range(1, n+1)}
        self.rank = {i: 1 for i in range(1, n+1)}

    def find(self, x):
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]
        return x

    def union(self, x, y):
        xroot, yroot = self.find(x), self.find(y)
        if xroot != yroot:
            if self.rank[xroot] > self.rank[yroot]:
                self.root[yroot] = xroot
            elif self.rank[yroot] > self.rank[xroot]:
                self.root[xroot] = yroot
            else:
                self.root[yroot] = xroot
                self.rank[xroot] += 1


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UnionFind(n)

        for u, v, w in roads:
            uf.union(u, v)

        root1 = uf.find(1)
        res = float("inf")

        for u, v, w in roads:
            if uf.find(u) == root1:
                res = min(res, w)

        return res
