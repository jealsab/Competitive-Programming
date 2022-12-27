class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        k=len(nums)-3
        while k>=0:
            if nums[k]+nums[k+1]>nums[k+2]:
                return nums[k]+nums[k+1]+nums[k+2]
            k-=1
        return 0

        