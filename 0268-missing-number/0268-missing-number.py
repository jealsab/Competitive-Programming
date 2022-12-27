class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=Counter(nums)
        n=len(nums) #2
        for i in range(n+1):
            if i not in count:
                return i