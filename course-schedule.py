class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        incoming = [0 for _ in range(numCourses)]
        queue = deque()
        total = 0
        for course, pre in prerequisites:
            graph[pre].append(course)
            incoming[course] += 1
        for course in range(numCourses):
            if incoming[course] == 0:
                queue.append(course)
        while queue:
            course = queue.popleft()
            total+=1
            for neighbor in graph[course]:
                incoming[neighbor] -= 1
                if incoming[neighbor] == 0:
                    queue.append(neighbor)
        if total == numCourses:
            return True
        return False