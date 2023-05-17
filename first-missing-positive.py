class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums= list(set(nums))
        heapq.heapify(nums)
        cur_pos= 1
        while nums:
            n = heapq.heappop(nums)
            if n>0 and n != cur_pos:
                return cur_pos
            elif n<=0:
                continue
            else:
                cur_pos+=1
        return cur_pos