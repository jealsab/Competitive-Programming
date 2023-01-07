class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        pairs = 0

        for i in range (n):
            for j in range (n):
                flag=0
                for k in range (n):
                    if grid[i][k]==grid[k][j]:
                        pass
                    else:
                        flag=1
                        break
                if flag==0:
                    pairs+=1
        return pairs
               