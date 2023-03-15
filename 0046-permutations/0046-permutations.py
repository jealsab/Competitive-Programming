class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =[]
        permutation=[]
        used=set()
        self.backtrack(res,nums,permutation,used)
        return res
    def backtrack(self,res,nums,permutation,used):
        if len(permutation)==len(nums):
            res.append(permutation)
            return
        for i in range (len(nums)):
            if i not in used:
                used.add(i)
                self.backtrack(res,nums,permutation+[nums[i]],used)
                used.remove(i)
        
        
      