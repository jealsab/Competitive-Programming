class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        m=len(grid[0])
        row01=[]
        col01=[]
        for i in range(n):
            zero=0
            one=0
            for j in range(m):
                if grid[i][j] ==0:
                    zero+=1
                else:
                    one+=1
            row01.extend([one])
            
        for i in range (m):
            zero=0
            one=0
            for j in range (n):
                if grid[j][i]==0:
                     zero+=1
                else:
                    one+=1
            col01.extend([zero])
          
        diff = [[0 for l in range(m)]for k in range(n)]
        for i in range (0,n):
            for j in range (0,m):
                diff[i][j] = (row01[i] - (m-row01[i])) +((n-col01[j]) - col01[j])

          
        return diff
    
   #                 
#                 2-1+1-2
# 2-1+1-2  `                    [0,0]
# 2-1+3-0-0