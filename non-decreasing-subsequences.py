class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """  
        def backtrack(i):
            if i == len(nums):
                if len(ans) >= 2:
                    res.add(tuple(ans))
                return
            if not ans or ans[-1] <= nums[i]:
                ans.append(nums[i])
                backtrack(i + 1)
                ans.pop()
            backtrack(i + 1)

        res = set()
        ans = []
        backtrack(0)
        return res