class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        incoming = [0 for _ in range(numCourses)]
        order = []

        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1
        
        queue = deque()
        for course in range(numCourses):
            if incoming[course] == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            order.append(course)
            for c in graph[course]:
                incoming[c]-=1
                if incoming[c] == 0:
                    queue.append(c)

        if len(order) != numCourses:
            return []

        return order


