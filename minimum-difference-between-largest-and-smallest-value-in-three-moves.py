class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        nums.sort()
        j = len(nums)-4
        _min = float("inf")
        i = 0
        if len(nums)<=3:
            return 0
        else:
            while j<len(nums):
                # print(i)
                _min= min(_min,nums[j]-nums[i])
                i+=1
                j+=1
        return _min