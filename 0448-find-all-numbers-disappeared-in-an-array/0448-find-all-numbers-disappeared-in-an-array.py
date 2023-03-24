class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in nums:
            index=abs(i)-1
            nums[index]=-1 * abs(nums[index])
        res=[]
        for i,n in enumerate(nums):
            if n>0:
                res.append(i+1)
        return res
    