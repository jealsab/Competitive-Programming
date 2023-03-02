class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # window_size= len(s1)-1
        c1=Counter(s1)
        i=0
        j= len(s1)-1
        
        while i <len(s2) and j < len(s2):
                # print(Counter(s2[i:j+1]))
                if c1 == Counter(s2[i:j+1]):
                    return True
                i+=1
                j+=1
        return False
    
    
        
        # "ab" {a:1,b:1}
        # "eidbaooo" {i:1,b:2} if c1==c2 return true else
         #  ij