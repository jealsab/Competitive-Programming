# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        def countPath(root , curr, targetSum):
            if root is None:
                return 0
            res = 0
            curr += root.val
            
            if curr-targetSum in dic:
                res += dic[curr-targetSum]
                
            if curr in dic:
                dic[curr]+=1
                
            else:
                dic[curr] = 1
            res+=countPath(root.left,curr,targetSum)
            res+=countPath(root.right,curr,targetSum)
            
            dic[curr]-= 1
            
            return res
            
        dic = defaultdict(int)
        dic[0]=1
        return countPath(root,0,targetSum)
    