class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        res = 0
        oneGroup = sum(skill) // (n / 2)
        count=Counter(skill)
        
        if oneGroup*(n/2)!=sum(skill):
            return -1
            
        for i in range(n):
            
            x=int(oneGroup-skill[i])
            if count[skill[i]]<=0:
                continue
            count[skill[i]]-=1
            if x in count and count[x]>=0:
                count[x]-=1
                res+=x*skill[i]
            else:
                return -1
        return res
            
            
                                
            
            
        
        
        
        
        
         # [3,2,5,1,3,4]
            
            
   
















