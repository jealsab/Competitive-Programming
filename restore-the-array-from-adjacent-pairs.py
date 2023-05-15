class Solution(object):
    def restoreArray(self, adjacentPairs):
        """
        :type adjacentPairs: List[List[int]]
        :rtype: List[int]
        """
        indegree={}
        for i in range(len(adjacentPairs)):
            indegree[adjacentPairs[i][0]]=0
            indegree[adjacentPairs[i][1]]=0
        print(indegree)
        graph = defaultdict(list)
        q =[]
        for i in range (len(adjacentPairs)):
            graph[adjacentPairs[i][0]].append(adjacentPairs[i][1])
            indegree[adjacentPairs[i][0]]+=1
            graph[adjacentPairs[i][1]].append(adjacentPairs[i][0])
            indegree[adjacentPairs[i][1]]+=1
        # print(indegree)
        for key, value in indegree.items():
            if 1 == value:
                q.append(key)
        # print(q)
        # print(graph)
        res=[]
        while q:
            # print(q)
            n = q.pop()
            res.append(n)
            for child in graph[n]:
                indegree[child]-=1
                if indegree[child]==1:
                    q.append(child)
        return (res)
                
        # if indegree[i]==1:
                # stk.append(i)
        # for i in stack:
        #     indegree[i]-=1
        #     if len(graph[i])== 1:
        #         stk.append(graph[i])