class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        
        # [-3,4,3,2], pivot = 2
        low=[]
        pivots=[]
        high=[]
        
        for i in range(len(nums)):
                if nums[i]<pivot:
                    low.append(nums[i])
                elif nums[i]==pivot:
                    pivots.append(nums[i])
                else:
                    high.append(nums[i])
                
        low.extend(pivots)
        low.extend(high)
        return(low)