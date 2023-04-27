class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        def bfs(node):
            queue = deque([0])
            visited = set([0])
            
            while queue:
                node = queue.popleft()
                
                for i in rooms[node]:
                    if i not in visited:
                        queue.append(i)
                        visited.add(i)
            return visited

        v = bfs(0)
        for i in range(len(rooms)):
            if i not in v:
                return False
            
        return True