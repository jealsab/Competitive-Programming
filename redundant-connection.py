class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        root ={} 
        size = {}
        for a, b in edges:
            root[a]=a
            size[a]=1
            root[b]=b
            size[b]=1
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if size[rootX]>size[rootY]:
                    root[rootY]=rootX
                    size[rootX]+=rootY
                else:
                    root[rootX]=rootY
                    size[rootY]+=rootX
            else:
                return [x,y]


        for a,b in edges:
            res = union(a,b)
            if res:
                return res
        return res