class Solution(object):
    def maxSum(self, grid):
        """

        :type grid: List[List[int]]
        :rtype: int
        """
       
        m = len(grid)
        n = len(grid[0])
        res = 0
        
        for i in range(m-2):
            for j in range(n-2):
                total = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                total += grid[i+1][j+1]
                total += grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                
                res = max(res, total)
                
        
        return res