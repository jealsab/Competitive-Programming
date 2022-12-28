class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        d={}
        winner=[]
        looser=[]
        for i in range (len(matches)):
            if matches[i][1] not in d:
                d[matches[i][1]]=1
            else:
                d[matches[i][1]]+=1
        # print()
        for i in range (len(matches)):
            if matches[i][0] not in d:
                winner.append(matches[i][0])

        for l, c in d.items():
            if c==1:
                looser.append(l)
        looser.sort()
        winner=list(set(winner))
        winner.sort()
        return[winner,looser]



    