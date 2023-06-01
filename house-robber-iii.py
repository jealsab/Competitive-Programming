# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):

        # @cache
        memo = {}

        def bfs(node,flag):
            if not node:
                return 0
            if (node,flag) in memo:
                return memo[(node,flag)]
            
            if flag:
                option1 = node.val+bfs(node.left,False)+bfs(node.right,False)
                option2 = bfs(node.left,True)+bfs(node.right,True)
                memo[(node,flag)]=max(option1,option2)
                return memo[(node,flag)]
            memo[(node,flag)]= bfs(node.right,True)+bfs(node.left,True)
            return memo[(node,flag)]
            
        return bfs(root,True)