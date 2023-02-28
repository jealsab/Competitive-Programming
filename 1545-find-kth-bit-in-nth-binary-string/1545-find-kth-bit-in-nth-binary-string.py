class Solution:
    def findKthBit(self, n: int, k: int) -> str:
      
        def invert(S):
            s = ""
            for i in S:
                if i == '0':
                    s += '1'
                else:
                    s += '0'
            return s
    
        def findKthbit(n):
            
            if n == 1:
                return '0'
            
            S = findKthbit(n-1)
            return S + '1' + invert(S)[::-1]
        
        return findKthbit(n)[k-1]
    
    
    
    
  