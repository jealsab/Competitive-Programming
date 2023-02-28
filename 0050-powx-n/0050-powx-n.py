class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        elif n > 0:
            if n == 1:
                return x
            elif n % 2 == 0:
                y = self.myPow(x, n/2) 
                return  y * y
            else:
                return x * self.myPow(x,n-1)
               
        else:
            return self.myPow(1/x,-n)