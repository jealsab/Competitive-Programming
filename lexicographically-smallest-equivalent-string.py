class Solution(object):
    def smallestEquivalentString(self, s1, s2, baseStr):
        """
        :type s1: str
        :type s2: str
        :type baseStr: str
        :rtype: str
        """
        root = {chr(x): chr(x) for x in range(ord("a"), ord("z") + 1)}
       
        
        # print(root)
        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(a , b):
            rootA= find(a)
            rootB=find(b)
            if rootA != rootB:
                if ord(rootA) < ord(rootB) :
                        rootA,rootB = rootB,rootA
                root[rootA] = rootB
                            
        for x,y in zip(s1,s2):
            union(x,y)

        res = ""
        for ch in baseStr:
            r = find(ch)
            res += r
        return res