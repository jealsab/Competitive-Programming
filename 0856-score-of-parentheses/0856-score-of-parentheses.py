class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[]
        res = 0
        val = 0 
        for c in s:
            
            if c== "(":
                stack.append(0)
                
            elif c == ")":
                m = stack.pop()
                
                if m == 0:
                    val = 1
                    
                else:
                    val= m*2
                    
                if  stack == [] :
                    res+=val
 
                else: 
                    stack[-1]+=val
        return res