class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
"""
        visited = set()  
        def dfs(isConnected, visited, i):
            if i in visited:  
                return 0
            visited.add(i) 
            for j in range(len(isConnected[i])):  
                if isConnected[i][j] == 1:
                    dfs(isConnected, visited, j)  
            return 1  
        no_provinces = 0  
        for i in range(len(isConnected)): 
            no_provinces += dfs(isConnected, visited, i) 
        return no_provinces