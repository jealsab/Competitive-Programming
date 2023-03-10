# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def preorder(node: TreeNode, path: str):

            if path == "": 
                path += str(node.val)
            else: 
                path += "->" + str(node.val)

            if node.left: 
                preorder(node.left, path)
            if node.right: 
                preorder(node.right, path)
            if not node.left and not node.right:
                paths.append(path)

        preorder(root, "")

        return paths
