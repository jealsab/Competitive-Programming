class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(nums)-1
        res = []
       
        while left <= right:
            
            mid = (left + right) // 2
            
            if nums[mid] < target:
                left = mid + 1
                
            elif nums[mid] > target :
                right = mid -1 
                
            else:
                
                if nums[left] < target:
                    left = left + 1
                if nums[right] > target:
                    right = right -1 
               
                if nums[left] == target and nums[right] == target:
                    res.append(left)
                    res.append(right)
                    break
        if len(res)!=0:
            return res
        return [-1,-1]
    # [5,7,7,8,8,10] mid = (3 + 5) // 2 == 4
     #       l m  r
