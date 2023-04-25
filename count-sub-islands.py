class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        
        
        def dfs(i,j):
            if i<0 or i>=len(grid1) or j<0 or j>=len(grid1[0]) or grid2[i][j]==0:
                return
            
            grid2[i][j]=0
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i-1,j)
            
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j]==1 and grid1[i][j]==0:
                    dfs(i,j)
        
        c=0
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid2[i][j]==1:
                    dfs(i,j)
                    c+=1
        return c