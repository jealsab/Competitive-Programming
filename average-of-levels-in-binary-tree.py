# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        def bfs(node):
            ans=[]
            queue = deque([node])
            while queue:
                cur_level=len(queue)
                level=[]
                for i in range(cur_level):
                    nod=queue.popleft()
                    if nod.left:
                        queue.append(nod.left)
                    if nod.right:
                        queue.append(nod.right)
                    level.append(nod.val)
                print(level)
                # r = sum(level)
                res = (float(sum(level))/cur_level)
               
                ans.append(res)   
            return ans          
        

        return bfs(root)