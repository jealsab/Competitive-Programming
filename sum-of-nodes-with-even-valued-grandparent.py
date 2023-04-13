# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root,d,gp):
            if not root:
                return 0
            x=0
            if(gp%2==0):
                x=root.val
            x+=dfs(root.left,root.val,d)
            x+=dfs(root.right,root.val,d)
            return x

        return dfs(root,1,1)