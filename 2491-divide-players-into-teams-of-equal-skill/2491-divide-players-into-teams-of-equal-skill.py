class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
#         n=len(skill)/2
        n = len(skill)
        s = 0
        oneGroup = sum(skill) // (n / 2)
        count=Counter(skill)
        
        if oneGroup*(n/2)!=sum(skill):
            # print("no")
            return -1
    
            
        for i in range(n):
            
            x=int(oneGroup-skill[i])
            print(x,skill[i],count[x],count[skill[i]])
            # print(skill[i])
            if count[skill[i]]<=0:
                continue
            count[skill[i]]-=1
            if x in count and count[x]>=0:
                count[x]-=1
                s+=x*skill[i]
            else:
                print(count[x])
                print(count[skill[i]])
                return -1
        return s
            
            
                                
            
            
        
        
        
        
        
         # [3,2,5,1,3,4]
            
            
   


















             
#     ans = 0
#     count = collections.Counter(skill)

#     for s, freq in count.items():
#       requiredSkill = teamSkill - s
#       if count[requiredSkill] != freq:
#         return -1
#       ans += s * requiredSkill * freq

#     return ans // 2