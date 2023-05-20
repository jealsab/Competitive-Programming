# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                return ''
            
            c = str(node.val)
            if not node.left and not node.right:
                return c
            
            c += '(' + dfs(node.left) + ')'
            if node.right:
                c += '(' + dfs(node.right) + ')'
            
            return c
   
        return dfs(root)