class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        
        # [-3,4,3,2], pivot = 2
        l=[]
        e=[]
        g=[]
        
        for i in range(len(nums)):
                if nums[i]<pivot:
                    l.append(nums[i])
                elif nums[i]==pivot:
                    e.append(nums[i])
                else:
                    g.append(nums[i])
                
        l.extend(e)
        l.extend(g)
        return(l)