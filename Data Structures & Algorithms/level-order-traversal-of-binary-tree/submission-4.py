# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        final = []
        queue = []
        if root:
            queue.append([root])
        i=0
        while i<len(queue):
            curr = []
            nexty=[]
            for r in queue[i]:
                curr.append(r.val)
                if r.left:
                    nexty.append(r.left)
                if r.right:
                    nexty.append(r.right)
            final.append(curr)
            if len(nexty)>0:
                queue.append(nexty)
            i+=1
            
        return final
            



        