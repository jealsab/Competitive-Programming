class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        
        
        par = [i for i in range(len(accounts))]
        rank = [1] *len(accounts)
    
        def find( x):
            if x != par[x]:
                par[x] = find(par[x])
            return par[x]
        
        def union( x1, x2):
            
            p1 = find(x1)
            p2 = find(x2)
            if p1 == p2:
                return 0
            if rank[p1] < rank[p2]:
                p1,p2=p2,p1
            
            par[p1] = p2
            rank[p2] += rank[p1]
            return 1

        parent = {} 

        for i, j in enumerate(accounts):
            for e in range(1,len(j)):
                if j[e] in parent:
                    union(i, parent[j[e]]) 
                else:
                    parent[j[e]] = i


        components = defaultdict(list) 
        for e, i in parent.items():
            components[find(i)].append(e) 

        res = []
        for i, emails in components.items():
            name = accounts[i][0] 
            res.append([name] + sorted(components[i])) 
        return res