class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        l=len(grid)-2
        result= [[0]*(l) for i in range (l)]
        for i in range (l):
            for j in range(l):
                 for inneri in range(i, i+3): 
                        for innerj in range(j, j+3):
                            result[i][j] = max(grid[inneri][innerj],result[i][j])
        return result