class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        for windowStart in range( n - m  + 1) :
            for  i in range ( m):
                if needle[i] != haystack[windowStart + i]:
                    break
                
                if i == m - 1:
                    return windowStart
          

        return -1;
   