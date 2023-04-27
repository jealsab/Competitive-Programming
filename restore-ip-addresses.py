class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)

        if not (4 <= n <= 12):
            return []

        res = []
        def backtrack(i, ip):

            if i == n or len(ip) == 4:

                if i == n and len(ip) == 4:
                    res.append(".".join(ip))

                return

            for j in range(i + 1, min(i + 4, n + 1)):
                if int(s[i:j]) > 255:
                    return
                ip.append(s[i:j])
                backtrack(j, ip)
                ip.pop()

                if s[i] == "0":
                    return

        backtrack(0, [])

        return res