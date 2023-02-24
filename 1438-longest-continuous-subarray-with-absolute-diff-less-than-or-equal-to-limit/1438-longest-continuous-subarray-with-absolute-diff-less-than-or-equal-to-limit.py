class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # [8,2,4,7] limit=4
        max_q=deque()
        min_q=deque()
        res=0
        i=0
        j=0
        
        while j< len(nums):
            while max_q and max_q[-1] < nums[j]:
                max_q.pop()
            max_q.append(nums[j])
            while min_q and min_q[-1] > nums[j]:
                min_q.pop()
            min_q.append(nums[j])
            while max_q and min_q and max_q[0] - min_q[0] > limit:
                if max_q[0] == nums[i]: 
                    max_q.popleft()
                if min_q[0] == nums[i]: 
                    min_q.popleft()
                i += 1
                
            res = max(res, j-i + 1)
            j += 1
        return res
        
            
        
        
#         if max_q and min_q==[]:
#             max_q.append(nums[0])
#             min_q.append(nums[0])
#         j = 0
#         for i in range (len(nums)-1):
#             if nums[i] < min_q[0] :
#                         min_q.popleft()
#                         min_q.append(nums2[i])
#             if nums[i] > max_q[0]:
#                         max_q.popleft()
#                         max_q.append(nums2[i])
#             while j< len(nums):
               
#                 if max_q[0]-min_q[0]<=limit:
#                     res=max(res,j-i+1)
               
#                 j+=1
#         return res


#        