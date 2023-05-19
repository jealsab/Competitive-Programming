class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        """
        :type recipes: List[str]
        :type ingredients: List[List[str]]
        :type supplies: List[str]
        :rtype: List[str]
        """
        graph = defaultdict(list)
        queue = deque(supplies)
        res = []
        incoming = defaultdict(int)
    
            
        for i in range(len(recipes)):
            for j in ingredients[i]:
                graph[j].append(recipes[i])
                incoming[recipes[i]] += 1
                
        while queue:
            node = queue.pop()
            if node in recipes:
                res.append(node)
            for n in graph[node]:
                incoming[n] -= 1
                if incoming[n] == 0:
                    queue.append(n)
                    
        return res