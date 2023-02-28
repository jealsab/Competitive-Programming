class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        
        """  

        def revStr(s, i=0 , j=len(s)-1):
            if i > j:
                return None
            else:
                s[i], s[j] = s[j], s[i]
                
            revStr(s,i+1,j-1)
            
        return revStr(s)
    
        
        
        
        
        
        
        
        
        
        # i=0
        # j=len(s)-1
        # while i<=j:
        #     s[i],s[j]=s[j],s[i]
        #     i+=1
        #     j-=1
        # return s