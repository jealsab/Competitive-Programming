class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(edges)):
            src, dest = edges[i][0], edges[i][1]
            graph[src].append((dest))
            graph[dest].append((src))
        for i in graph:
            if len(graph[i])==len(edges):
                return i