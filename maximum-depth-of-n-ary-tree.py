"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0
            res = 0
            for child in root.children:
                res = max(dfs(child),res)
            return res+1
        return dfs(root)