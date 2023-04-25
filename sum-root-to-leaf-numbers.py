# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(cur, n):
            if not cur:
                return 0
            
            n = n * 10 + cur.val
            if not cur.left and not cur.right:
                return n
            
            return dfs(cur.left, n) + dfs(cur.right, n)

        return dfs(root, 0)