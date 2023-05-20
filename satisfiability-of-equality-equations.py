class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        

        root = {}

        def find(x):

            if x not in root: 
                return x
            return find(root[x])

        def union(x,y):              
            x, y = find(a), find(b)
            if x!=y:
                root[y] = x

        for eq in equations:
            a, b = eq[0], eq[3]
            if eq[1] == '=':
               union( a,b)         
        
        for e in equations:
            a,b= e[0],e[3]
            if e[1] == '!':
                if find(a) == find(b):
                    return False
        
        return True