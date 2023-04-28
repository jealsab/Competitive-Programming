class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def inbound(r,c):
            return (0 <= r < len(grid) and 0 <= c < len(grid[0]))
        def bfs(r,c):
            
            visited = set([(r,c)])
            queue =  deque([[(r,c),1]])
            directions= [(0, 1), (0, -1), (1, 0), (-1, 0), (1 , 1),(-1 , -1),(-1 , 1),(1 , -1)]
            while queue:
                # print(queue)
                ((row, col), d) = queue.popleft()
                if row == len(grid)-1 and col == len(grid[0])-1:
                    return d

                
                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change
                    if inbound(new_row,new_col) and (new_row,new_col) not in visited and grid[new_row][new_col]==0:
                        visited.add((new_row,new_col))
                        queue.append([(new_row,new_col),d+1])
                    
            return -1
        

        if grid[0][0]==1:
            return -1
          
       
        return bfs(0,0)