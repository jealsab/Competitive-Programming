class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l =[]
        for i in range(1, threshold):
            l.append(i)
          
        nums.sort()
        left = 1
        right = nums[len(nums)-1]
        best = -1
        
        while left <= right :
           
            mid = (left+right)//2
            s = 0
            for num in nums:
                s += ceil(num/mid)
                
            if s > threshold:
                left = mid + 1
                
            else: 
                best = mid 
                right = mid - 1
                
        return best
       
#         1 2 3 4 5 6
#         1+6 = 7//2  3
#         1/3 + 2/3 + 5/3 + 9/3
#         1 + 1 + 2 + 3 = 7
        
        
        
        
        
