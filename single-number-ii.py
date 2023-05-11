class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        y = 0
        for i in nums:
            x = (x ^ i) & ~y
            y = (y ^ i) & ~x
        return x