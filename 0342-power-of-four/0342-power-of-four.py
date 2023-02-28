class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n==0:
            return False
        elif n==1 or n==4:
            return True
        elif n % 4 ==0:
            return self.isPowerOfFour(n/4)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#             def powOfFour(n):
#             if n == 0 : 
#                 return False
#             elif n == 1 or n == 4: 
#                 return True
#             elif n%4 == 0:
#                 return powOfFour(n/4)
        
#         return powOfFour(n)