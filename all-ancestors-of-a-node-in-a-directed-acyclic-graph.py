class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """

        graph = defaultdict(list)
        indegree = [0]*n
        res = [set() for _ in range(n)]

        for i in edges:
            graph[i[0]].append(i[1])
            indegree[i[1]] += 1
        queue = deque()
        for i in range(len(indegree)):
			if not indegree[i]:
				queue.append(i)
        while queue:
			node = queue.popleft()
			
			for child in graph[node]:
				indegree[child] -= 1
				res[child].add(node)
				
				for j in res[node]:
					res[child].add(j)
				if not indegree[child]:
					queue.append(child)
					
        for i in range(len(res)):
			res[i] = sorted(res[i])
        return res