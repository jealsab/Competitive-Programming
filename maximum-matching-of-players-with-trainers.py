class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        heapq.heapify(players)
        heapq.heapify(trainers)
        count = 0
        curr =  heapq.heappop(players)
        while trainers:
            nx = heapq.heappop(trainers)
            if curr <= nx:
                count += 1
                if players:
                    curr =  heapq.heappop(players)
                else:
                    break
        return count