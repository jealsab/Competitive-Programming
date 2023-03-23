class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        adj=defaultdict(list)
        for ele1,ele2 in connections:
            adj[ele1].append(ele2)
            adj[ele2].append(ele1)
        self.cables=0
        def dfs(i,visited,adj,parent):
            if(i in visited):
                self.cables+=1
                return
            visited.add(i)
            for child in adj[i]:
                if child!=parent:
                    dfs(child,visited,adj,i)
        c=0
        visited=set()
        for i in range(n):
            if i not in visited:
                c+=1
                dfs(i,visited,adj,-1)
        if(self.cables//2>=c-1):
            return c-1
        return -1
