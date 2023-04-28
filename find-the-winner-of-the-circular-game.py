class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        queue = deque()
        for i in range(1,n+1):
            queue.append(i)
            
        while len(queue) > 1:       
            for i in range(k-1):   
                temp = queue.popleft()
                queue.append(temp)
            queue.popleft()
        return queue[0]