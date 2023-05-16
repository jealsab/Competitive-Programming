class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        root = [i for i in range(n)]
        def find(x):
            while x != root[x]:
                x = root[x]
            return x
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                root[rootY] = rootX
        def connected(s, d):
            return find(s) == find(d)

        for i in range(len(edges)):
            union(edges[i][0],edges[i][1])
        return connected(source,destination)