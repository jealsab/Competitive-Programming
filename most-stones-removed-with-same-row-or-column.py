class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """   
       
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
            
        def union(x,y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX]<rank[rootY]:
                    rootX,rootY= rootY,rootX
                parent[rootY]=rootX
                rank[rootX]+=rootY
            
           
        
        n=len(stones)
        mr=mc=0
        for i,j in stones:
            mr=max(mr,i)
            mc=max(mc,j)
        parent=[i for i in range(mr+mc+2)]
        rank=[1 for i in range(mr+mc+2)]
        d= defaultdict(int) 
        for i,j in stones:
            union(i,j+mr+1)
            d[i]=1
            d[j+mr+1]=1
        c=0 
        for i in d:
            if find(i)==i:
                c+=1
        return n-c