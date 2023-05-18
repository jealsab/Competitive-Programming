class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
       
        def dfs(r,c):
            if 0>r or r>=len(grid) or 0>c or c>=len(grid[0]) or grid[r][c]==0:
                return 0
            grid[r][c] = 0
            return 1+dfs(r-1,c)+dfs(r+1,c)+dfs(r,c-1)+dfs(r,c+1)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    ans=max(ans,dfs(i,j))
        return ans