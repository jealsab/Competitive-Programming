class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        s=list(set(edges[0]) & set(edges[1]))
        return s[0]
               
                
            # [[1,2],[2,3],[4,2]]