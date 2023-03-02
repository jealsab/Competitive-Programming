class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
            res=[-1]*len(nums)
            index=[]
            for i in range(2*(len(nums))):
                while index!=[] and nums[index[-1]] < nums[i%len(nums)]:
                    res[index[-1]]=nums[i % len(nums)]
                    index.pop()
                index.append(i % len(nums))
                    
            return res
                    
            
         
 #            res=[-1]*len(nums)            
                    
#             stack = [nums[0]]
#             for i in range(0,len(nums)-1):
#                 if nums[i]<nums[i+1]:
#                     stack.pop()
#                     stack.append(nums[i+1])

#                     nums[i]=stack[-1]
#                     print(stack)
             
#             
           
#             return nums
                
        