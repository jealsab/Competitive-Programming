# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        def recurse(root,row,col):
            if not root:
                return 
            
            dic[col].append((row,root.val))
            recurse(root.left, row + 1 , col - 1)
            recurse(root.right, row + 1, col + 1)
             
            return dic  

        row = 0
        col = 0
        ans = []
        dic = defaultdict(list)
        recurse(root, row, col)
        
        for node in sorted(dic.keys()):
            final = []
            for f in sorted(dic[node]):
                final.append(f[1])
            ans.append(final)
        return ans
    
       
    
                    
