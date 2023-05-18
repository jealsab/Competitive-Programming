class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        root ={} 
        size = {}
        _min = {i: float("inf") for i in range(1, n+1)}

        for i in range(len(roads)):
            a , b=roads[i][0],roads[i][1]
            root[a]=a
            size[a]=1
            root[b]=b
            size[b]=1

        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        def union(x, y ,w):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if size[rootX]<size[rootY]:
                    rootX,rootY= rootY,rootX
                root[rootY]=rootX
                size[rootX]+=rootY
            _min[rootX] = min(_min[rootX], w,_min[rootY])
           

        for a,b,w in roads:
            res = union(a,b,w)
        return _min[find(1)]