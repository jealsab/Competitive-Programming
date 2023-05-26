class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = {0:0,1:1,2:1}
        def func(i):
            if i in memo:
                return memo[i]
            memo[i]= func(i-1)+func(i-2)+func(i-3)
            return memo[i]
        return func(n)