class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        lst = []
        matrix = []

        for s in mat:
            for i in s:
                lst.append(i)

        if len(lst) != r * c:
            return mat
        else:
            for i in range (0,len(lst),c):
                matrix.append(lst[i:i+c])
            return matrix