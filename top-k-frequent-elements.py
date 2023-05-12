class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        count = Counter(nums)
        sets =  set(nums)
        temp = []
        for i in sets:
            heapq.heappush(temp,(-count[i],i))
        # print(temp)
        res = []
        while k:
            n = heapq.heappop(temp)
            res.append(n[1])
            k-=1
        return res