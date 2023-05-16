class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
       
        l = {c: i for i, c in enumerate(s)}
        a = 0
        j = a
        ans = []
        for i, c in enumerate(s):
            j = max(j, l[c])
            if i == j:
                ans.append(i - a + 1)
                a = i + 1
            
        return ans