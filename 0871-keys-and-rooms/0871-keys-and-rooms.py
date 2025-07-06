class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        graph = defaultdict(list)
        n = len(rooms)  

        visited = [False] * n

        for i in range(len(rooms)):
            graph[i]
            for neighbor in rooms[i]:
                graph[i].append(neighbor)
        queue = deque()
        queue.append(0)
        visited[0] = True
        while queue:   
            for _ in range(len(queue)):
                room = queue.popleft()
                for neighbor in graph[room]:
                    if  not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
        return all(visited)
  
