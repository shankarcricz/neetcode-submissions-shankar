# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  

    def checkIfSame(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None: return False
        if root2 is None: return False
        print(root1.val, root2.val)

        if root1.val != root2.val: return False
        
        return self.checkIfSame(root1.left, root2.left) and self.checkIfSame(root1.right, root2.right)
        


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None: return False
        if root.val == subRoot.val:
            if self.checkIfSame(root, subRoot): return True
          
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
       


        