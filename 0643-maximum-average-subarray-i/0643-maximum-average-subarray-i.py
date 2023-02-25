class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        total = sum(nums[0:k])
        ans = total

        for i in range (k, len(nums)):
            total = total - nums[i-k] + nums[i]
            ans = max(ans, total)

        return ans/k