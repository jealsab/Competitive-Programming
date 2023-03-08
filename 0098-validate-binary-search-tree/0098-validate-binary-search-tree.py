# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return None
        
        def validBST(root ,l , r):
            if root == None:
                return True
            if root.val <= l or root.val >= r:
                return False
            
            left = validBST(root.left, l, root.val)
            right = validBST(root.right, root.val, r)
            
            return left and right
        
        return validBST(root,float("-inf"),float("inf"))