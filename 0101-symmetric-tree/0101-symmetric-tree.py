# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def helper(left , right):
            if left is None and right is None :
                return True
            if left is None or right is None:
                return False
            if left.val == right.val:
                Left = helper(left.left,right.right)

                Right = helper(left.right, right.left)
                
                return Left and Right
            else: return False
        if not root:
            return False
        return helper(root.left, root.right)
            