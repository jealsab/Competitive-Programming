class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res=''
        size=len(nums)
        for i in range (0,size-1):
            for j in range(i+1,size):
                if str(nums[i])+str(nums[j])<str(nums[j])+str(nums[i]):
                    nums[i],nums[j]=nums[j],nums[i]
        if nums[0] == 0: 
            return '0'
        for k in range (0,size): 
            res += str(nums[k])
            k+=1               
        return res 
