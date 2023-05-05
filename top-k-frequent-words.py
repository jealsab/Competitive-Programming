class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        c = Counter(words)
        h =[]
        for i in c:
            h.append((-c[i],i))
        heapq.heapify(h)

        res =[]
        for i in range(k):
            print(h)
            r = heapq.heappop(h)
            res.append(r[1])
        return (res)