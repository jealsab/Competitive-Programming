class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        
        def rec(i,nums):
                if i >= len(nums):
                    return -1
                if nums[i]==target:
                    return i
                else:
                    return rec(i+1,nums)
        return rec(0, nums)
            # mid =(low +high)//2
            # if low > high:
            #     return -1
            # if nums[mid] < target:
            #     return rec(mid+1, high, nums)
            # elif nums[mid] > target:
            #     return rec(low, mid-1, nums)
            # elif nums[mid] == target:
            #     return mid
            
               
        # return rec(0,len(nums)-1,nums)
    
           