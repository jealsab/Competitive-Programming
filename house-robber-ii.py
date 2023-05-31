class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return 1
        '''
        Since House[1] and House[n] are adjacent, they cannot be robbed together. Therefore, the problem becomes to rob either House[1]-House[n-1] or House[2]-House[n], depending on which choice offers more money. Now the problem has degenerated to the House Robber, which is already been solved.
        '''
        if len(nums) < 4:
            return max(nums)
        def rob(nums):
            dp = [float("-inf") for i in range(len(nums))]
            dp[0] = nums[0]
            dp[1]= max(nums[0], nums[1])
            for i in range(2,len(dp)):
                dp[i]=max(nums[i]+dp[i-2], dp[i-1])
            return dp[-1]
            
        return max(rob(nums[1:]), rob(nums[:-1]))