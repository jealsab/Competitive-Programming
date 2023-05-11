class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        building = 0
        heap=[]
        for i in range(len(heights)-1):            
            x = heights[i+1]-heights[i]
            if x>0:
                heappush(heap,x)
                if len(heap)>ladders:
                    bricks-=heappop(heap)
                    if bricks<0:
                        return i
            building+=1
        return building