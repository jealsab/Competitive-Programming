class Solution(object):
    def maxSum(self, grid):
        """

        :type grid: List[List[int]]
        :rtype: int
        """
       
        r = len(grid)
        c = len(grid[0])
        res = 0
        
        for i in range(r-2):
            for j in range(c-2):
                hg = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
               
                
                res = max(res, hg)
                
        
        return res