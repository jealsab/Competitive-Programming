class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(node, path):
            if node == len(graph)-1:
                ans.append(path[:])
                return 

            for child in graph[node]:
                path.append(child)
                dfs(child,path)
                path.pop()
            
        
        path=[0]
        ans=[]
        dfs(0, path)
        return ans