class Solution(object):
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
       
        
        def f(i,x):
            if i==len(nums):
                count[x]+=1
                return
            
            f(i+1,x|nums[i])
            f(i+1,x)
        
        count=Counter()
        f(0,0)
        
        _max=max(count)
        return count[_max]