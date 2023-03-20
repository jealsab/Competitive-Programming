# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(match, flipper):
            
            if not match and not flipper:
                return True
            
            if not (match and  flipper):
                return False
            
            if match.val != flipper.val:
                return False
            
            regular = dfs(match.left, flipper.left) and dfs(match.right, flipper.right)
            
            flipped = dfs(match.left, flipper.right) and dfs(match.right, flipper.left)
            
            return regular or flipped
        
        return dfs(root1, root2)