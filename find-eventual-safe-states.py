class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        q = deque()
        grph = defaultdict(list)
        outgoing= [0 for _ in range (len(graph))]
        # print(len(graph))
        res =[]
        for i in range(len(graph)):
            outgoing[i]=len(graph[i])
            for j in graph[i]:
                grph[j].append(i)
            if outgoing[i] == 0:
                q.append(i)

                
        while q:
            n = q.popleft()
            res.append(n)
            for child in grph[n]:
                outgoing[child]-=1
                if outgoing[child]==0:
                    q.append(child)
        return sorted(res)


        
        



        
       
        # q =deque()
        # for i in range(len(graph)):
        #     if graph[i] == []:
        #         q.append(i)
        # res=[]
        # while q:
        #     n = queue.popleft()
        #     res.append(n)