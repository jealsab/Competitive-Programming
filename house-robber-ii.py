class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=3:
            return max(nums)

        dp1 = [0 for _ in range (len(nums)+1)]
        dp2= [0 for _ in range (len(nums)+1)]

        dp1[-2]= nums[-1]
        dp2[0] = nums[0]

        for i in range(len(nums)-2,-1,-1):
            if i!=0:
                dp1[i]=max(dp1[i+1],nums[i]+dp1[i+2])
            else:
                dp1[i] =max(dp1[i+1],dp1[i+2])
            # print(dp1)

        nums[-1]=0
        for i in range(len(nums)-2,-1,-1):
            dp2[i]=max(dp2[i+1],nums[i]+dp2[i+2])
            
            # print(dp2)


        return max(dp1[0],dp2[0])