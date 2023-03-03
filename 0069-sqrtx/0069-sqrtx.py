class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        best =-1
        while l<=r:
            mid=(l+r)//2
            if mid*mid<=x:
                best=mid
                l = mid + 1                
            elif mid*mid>x:
                r=mid-1
            
        return best
           
        
