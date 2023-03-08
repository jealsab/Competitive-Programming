# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        
        dic = defaultdict(list)
        
        def preOrder(node,level):
            if node is None:
                return 
            
            dic[level].append(node.val)
            
            
            preOrder(node.left, level+1)
            preOrder(node.right,level+1)
            
           

            
            return ans
        ans = []
        preOrder(root , 1)
        
        for level in sorted(dic.keys()):
            ans.append(dic[level])
        return ans
        
    
    
    
    
    
    
    
    
    
    