class Solution(object):
    def distinctPrimeFactors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def isPrime(num, res): 
            i = 2
            
            while i * i <= num:
                while num % i == 0:
                    res.add(i)
                    num = num //i
                i += 1
            if num > 1:
                res.add(num)
        
        res =set()
        for num in nums:
            isPrime(num, res)
            
        return len(res)