class Solution(object):
    def getAncestors(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[List[int]]
        """
        graph= defaultdict(list)
        indegree = [0 for _ in range(n)]
        for i in range(len(edges)):
            indegree[edges[i][1]]+=1
            graph[edges[i][0]].append(edges[i][1])
        q = deque()
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        res = [set() for _ in range (n)]
        while q:
            n= q.popleft()
            for child in graph[n]:
                indegree[child]-=1
                res[child].add(n)
                res[child].update(res[n])
                if indegree[child] == 0:
                    q.append(child)
        return [sorted(i) for i in res]