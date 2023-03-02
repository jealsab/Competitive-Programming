class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for p in path.split("/"):
            if p == "" or p == ".": 
                continue
            elif p == ".." and stack: 
                stack.pop()
            elif p == "..": 
                continue
            else: 
                stack.append(p)
        
        return "/" + "/".join(stack)