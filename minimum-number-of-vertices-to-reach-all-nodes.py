class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        indegree = [0] * n  
        
        for edge in edges:
            indegree[edge[1]] += 1  
        # print(indegree)
        result = [] 
        
        for i in range(n):
            if indegree[i] == 0:
                result.append(i) 
        
        return result