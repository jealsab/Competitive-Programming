class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        visited = set((0,0))
        heap = [[nums1[0] + nums2[0],0,0]]
        res = []
        
        while heap and k:
           
            total, i, j = heappop(heap)
            res.append([nums1[i],nums2[j]])

            if i < len(nums1) - 1  and (i+1, j) not in visited:
                heappush(heap, [nums1[i + 1] + nums2[j],i+1, j])
                visited.add((i+1, j))
            
            if j < len(nums2) - 1 and (i, j+1) not in visited:
               heapq.heappush(heap, [nums1[i] + nums2[j+1],i, j + 1])
               visited.add((i, j+1))
            
            k -= 1
            
        return res