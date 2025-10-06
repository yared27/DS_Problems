class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for pre, course in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        prereq = [set() for _ in range(numCourses)]
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        while queue:
            course = queue.popleft()
            
            for next_course in graph[course]:
                prereq[next_course].add(course)
                prereq[next_course].update(prereq[course])
                
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        
        ans = []
        for u, v in queries:
            ans.append(u in prereq[v])
        return ans
