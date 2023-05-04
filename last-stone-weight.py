class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        for i in range(len(stones)):
            stones[i]= -stones[i]
        # print(stones)
        while len(stones)!=1:
            heapq.heapify(stones)
            # print(stones)
            if len(stones)==0:
                return 0
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x!=y:
                _max = max(x,y)
                x -= _max
                heapq.heappush(stones, x)
        
        return -stones[0]