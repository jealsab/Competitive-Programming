class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [0]*length
        for i in range(0, length):
            for j in range(0, length):
                if(nums[i]>nums[j]):
                    res[i]+=1
        return res