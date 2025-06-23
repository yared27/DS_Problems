class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = set()
        n=len(isConnected)
        def dfs(city):
            for neighbor in range(n):
                if isConnected[city][neighbor]==1 and neighbor not in visited:
                    visited.add(neighbor) 
                    dfs(neighbor)
        
        for  city in range(n):
            if city not in visited:
                dfs(city)
                provinces+=1
        return provinces
                    
                    




