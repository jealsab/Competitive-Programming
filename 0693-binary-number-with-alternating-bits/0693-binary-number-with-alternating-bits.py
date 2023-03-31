class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # print(n>>1)
        while n > 0 :
            if n % 2 == 0:
                n = n>>1
                if n % 2 ==0:
                    return False
                    
            if n % 2 != 0:
                n = n>>1
                if n%2 !=0:
                    return False
                
                    
        return True
            