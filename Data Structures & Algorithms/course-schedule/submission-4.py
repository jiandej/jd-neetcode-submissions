from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0]*numCourses

        for prerequisite in prerequisites:
            graph[prerequisite[1]].append(prerequisite[0])
            indegree[prerequisite[0]]+=1
        
        queue = collections.deque([i for i in range(numCourses) if indegree[i] == 0])
        count = 0
        
        while(queue):
            course = queue.popleft()
            count += 1

            for next_course in graph[course]:
                indegree[next_course] -= 1

                if (indegree[next_course] == 0):
                    queue.append(next_course)
        
        return count == numCourses
        
