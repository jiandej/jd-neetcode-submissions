class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegrees = [0]*numCourses
        
        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
            indegrees[prerequisite[0]] += 1
        
        queue = collections.deque([course for course in range(numCourses) if indegrees[course] == 0])

        result = []

        while (queue):
            course = queue.popleft()
            result.append(course)

            for next_course in graph[course]:
                indegrees[next_course] -= 1

                if (indegrees[next_course] == 0):
                    queue.append(next_course)
        
        return result if len(result) == numCourses else []
