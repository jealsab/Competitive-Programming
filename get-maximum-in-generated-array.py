class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return n
        arr = [0 for _ in range(n+1)]
        arr[0]=0
        arr[1]=1
        for i in  range (2,n+1):
            if i%2==0:
                arr[i]=arr[i/2]
            else:
                 arr[i]=arr[i/2]+arr[(i/2)+1]
        
        return max(arr)