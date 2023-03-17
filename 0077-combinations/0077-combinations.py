class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(j, curr):
            
            if len(curr) == k:
                res.append(curr[:])
                return
            for i in range(j,n+1):
                curr.append(i)
                
                backtrack(i+1,curr)
                
                curr.pop()
    
            
                
                
                
        # lst =[] 
        curr =[]
        res = []
        # for i in range(1,n+1):
        #     lst.append(i)
        backtrack(1 ,curr)
        return res