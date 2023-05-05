class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k=k
        self.h=nums
        heapq.heapify(nums)
        while len(self.h) > k:
            heapq.heappop(self.h)
    def add(self, val):
        """
        :type val: int
        :rtype: int
        """ 
        heapq.heappush(self.h, val)
        if len(self.h) > self.k:
            heapq.heappop(self.h)
        res = self.h[0]
        return res

        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)