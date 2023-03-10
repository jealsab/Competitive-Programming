class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(res, x):
            if not x:
                return True
			
            for i in range(1, n+1):
			
                if not res or int(x[:i]) == res[-1] - 1:
                    res.append(int(x[:i]))
					
                    if backtrack(res, x[i:]) and len(res) > 1:
                        return True
                    res.pop()

            return False
        n = len(s)
        return backtrack( [], s)
 