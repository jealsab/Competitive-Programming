class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=3:
            return max(nums)

        dp1 = [0 for _ in range (len(nums)-1)]

        dp1[0] = nums[0]
        dp1[1] = nums[1]
        dp1[2] = nums[2]+nums[0]
        
        for i in range(3, len(dp1)):
            dp1[i] = nums[i]+ max(dp1[0:i-1])  
        dp2 = [0 for _ in range (len(nums)-1)]

        dp2[0] = nums[1]
        dp2[1] = nums[2]
        dp2[2] = nums[1]+nums[3]
        
        for i in range(3, len(dp2)):
            dp2[i] = nums[i+1]+ max(dp2[0:i-1])  
        return max(max(dp1),max(dp2))