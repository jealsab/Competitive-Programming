class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
    
        def func(left, right, turn,nums):
            if left == right:
                return nums[left]* turn
            
            left_player = func(left+1,right,-turn,nums) + nums[left]*turn
            right_player = func(left,right-1,-turn,nums)+ nums[right]*turn
            
            if turn ==1:
                return max(left_player,right_player)
            
            return min(left_player,right_player)    
        return func(0,len(nums)-1, 1,nums) >=0

        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
         
        
        
        
        
