class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """  
        graph = defaultdict(list)
        
        indegrees = [0 for _ in range(numCourses)]
        for p,c in prerequisites:
            graph[p].append(c)
            indegrees[c] += 1
        
        queue = deque()
        for c in range(numCourses):
                if indegrees[c] == 0:
                    queue.append(c)

        res = defaultdict(set)
        while queue:
            p = queue.popleft()
            for c in graph[p]:
                indegrees[c] -= 1
                res[c].add(p)
                res[c].update(res[p])
                if indegrees[c] == 0:
                    queue.append(c)
        
        answer = []
        
        for u, v in queries:
            if u in res[v]:
                answer.append(True)
            else:
                answer.append(False)
                
        return answer