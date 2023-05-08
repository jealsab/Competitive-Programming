# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """

        if not preorder: 
            return
        if len(preorder) == 1: 
            return TreeNode(preorder[0])
        root = TreeNode(preorder[0])
        i = 1
        for j in range(1, len(preorder)):
            if preorder[j] < preorder[0]:
                i += 1
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root