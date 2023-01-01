class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res=[]
        even_sum=0
        for i in range (len(nums)):
            if nums[i]%2==0:
                 even_sum+=nums[i]
        
        for i in range(len(queries)):
            idx=queries[i][1]
            if nums[idx]%2==0:
                even_sum-=nums[idx]
            new=nums[idx]+queries[i][0]
            if new%2==0:
                even_sum+=new
            nums[idx]=new
            res.append(even_sum)
            
            
        return(res)

          