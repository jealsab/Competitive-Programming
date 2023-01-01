class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dict = {}
        for i in range(len(cpdomains)):
            cpd, domains = cpdomains[i].split()
            dot = 0
            while dot < len(domains.split(".")):
                last = domains.split(".", dot)
                if last[-1] in dict:
                    dict[last[-1]] += int(cpd)
                else:
                    dict[last[-1]] = int(cpd)
                dot += 1
        res = []
        for i in dict:
            res.append(str(dict[i]) + " " + i)
        return res