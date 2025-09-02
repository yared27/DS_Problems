class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        root = {i : i for i in range(n)}
        rank = [0]*n
        
        def find(x):
            while x != root[x]:
                root[x] = root[root[x]]
                x = root[x]
            return root[x]
        
        def union(x,y):
            xroot = find(x)
            yroot = find(y)

            if xroot != yroot:
                if rank[xroot] > rank[yroot]:
                    root[yroot] = xroot
                elif rank[yroot] > rank[xroot]:
                    root[xroot] = yroot
        
                else:
                    root[xroot] = yroot
                    rank[yroot] += 1
        def isConnectedCity(x,y):
            return root[x] == root[y]
        noProvinces = n
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] and find(i) != find(j):
                    noProvinces -= 1
                    union(i,j)
        

        return noProvinces

        




