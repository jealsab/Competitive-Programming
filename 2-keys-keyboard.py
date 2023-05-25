class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        d = 2
        while d*d <= n:
            while n % d == 0:
                res += d
                n //= d
            d += 1
        if n>1:
            res+=n
        return res