class Solution:    
    def findUnion(self, a, b):
        seen = set()  
        res = []

        for x in a:
            if x not in seen:
                seen.add(x)
                res.append(x)

        
        for x in b:
            if x not in seen:
                seen.add(x)
                res.append(x)

        return res
