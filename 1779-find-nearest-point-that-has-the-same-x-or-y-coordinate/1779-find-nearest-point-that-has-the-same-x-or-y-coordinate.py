class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        # [[1,2],[3,1],[2,4],[2,3],[4,4]]
        # x=3 y=4
        
        i=0
        d={}
        mah=float("inf")
        while i<len(points):
            if points[i][0]==x or points[i][1]==y:
                n=points[i][0]-x
                h=points[i][1]-y
                s=abs(n)+abs(h)
                mah=min(mah,s)
                d[i]=mah
            i+=1  
            
        output = float('inf')
        if len(d) != 0:
            for l, c in d.items():
                if c==mah :
                    output = min(output, l)
            return output
        else:
            return -1
        