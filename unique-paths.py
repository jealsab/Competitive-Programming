class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in range(n)] for j in range(m)]
        print(dp)
        dp[-1][-1] = 1
      
        def inbound(i, j):
           if 0 <= i < m and 0 <= j < n:
               return dp[i][j]
           return 0
       
        for r in range( m-1,-1,-1):
            for c in range(n-1,-1,-1):
                dp[r][c] += inbound(r + 1, c) + inbound(r, c + 1)
      
        return dp[0][0]