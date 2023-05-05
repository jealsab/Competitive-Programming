class Solution(object):
    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(piles)):
            piles[i]=-piles[i]
        heapq.heapify(piles)
    
        while k:
            # print(piles)
            s = heapq.heappop(piles)
            s= -((-s)-(-s//2))
            heapq.heappush(piles,s)
            k-=1
        
        return -(sum(piles))