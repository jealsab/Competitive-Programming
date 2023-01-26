class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        l = 0
        r = int(sqrt(c))
        while  l <= r:
            res =l**2 + r**2
            if res == c:
                return True
            elif res > c:
                r -= 1
            else:
                l += 1
        return False