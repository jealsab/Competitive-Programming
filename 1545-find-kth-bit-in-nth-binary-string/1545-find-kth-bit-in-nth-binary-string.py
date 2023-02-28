class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
#   converts '0'  to '1' and '1' to '0' & reverse(S)
        def invertReverse(S):
            s = ""
            for i in S:
                if i == '0':
                    s += '1'
                else:
                    s += '0'
            return s[::-1]
        
        
        def findKthbit(n):
        
        # base case
            if n == 1:
                return '0'
                
            S = findKthbit(n-1)
            return S + '1' + invertReverse(S)
        
        return findKthbit(n)[k-1]
    
    
    
    
  