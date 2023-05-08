class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        res=[]
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                res.append(matrix[i][j])
        heapq.heapify(res)

        while k:
            s = heapq.heappop(res)
            k -=1
             
        return s