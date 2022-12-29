class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        row=len(matrix)
        col=len(matrix[0])
        
        res=[[0]*row for i in range (col)]
        for i in range(row):
            for j in range(col):
                res[j][i]=matrix[i][j]
        return res
        # i,j=0,0
    
        # while j<col:
        #     while i<row:
        #         if i==j:
        #             pass
                
        #         matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        #         i+=1
        #     j+=1
        #     i=j
        # return matrix

            