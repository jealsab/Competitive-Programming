from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        #Code here
        colors = [0 for _ in range(V)]
        
        
        def dfs(node, parent):
            
            if colors[node] == 1:
                return True
            colors[node] = 1
            
                
            for child in adj[node]:
                if child == parent:
                    continue
                if dfs(child,node):
                    return True
                    
            colors[node] = 2
            return False
            
        for i in range(V):
            if colors[i] == 0:
                if dfs(i,-1):
                    return 1
        return 0
        
    
            
        
