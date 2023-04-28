class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        count = 0

        size = len(strs[0])

        for i in range(size):
            cur = strs[0][i]
            for str in strs[1:]:
                if str[i] < cur:
                    count += 1
                    break
                else:
                    cur = str[i]
        
        return count