# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        
        def Find(node):
            if node is None: 
                return None
            if node.val in dic:
                dic[node.val] += 1
            else: 
                dic[node.val] = 0
                
            Find(node.left)
            Find(node.right)
        dic = {}
        Find(root)
        _max = max(dic.values())
        a = []
        for num in dic:
            if dic[num] == _max :
                a.append(num)
        return a