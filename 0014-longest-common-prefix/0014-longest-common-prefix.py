class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        m = len(strs[0])
        for i in range(1, len(strs)):
            m = min(m, len(strs[i]))
        for i in range(0, m):
            cur = strs[0][i]
            for j in range(0, len(strs)):
                if strs[j][i] != cur:
                    return res
            res += cur
        return res