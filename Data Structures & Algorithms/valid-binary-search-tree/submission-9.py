# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def helper(self,root, l, b):
        if root is None: return True
        left = self.helper(root.left, l, root.val)
        right = self.helper(root.right,root.val, b)

        if root.val > l and root.val < b and left and right: return True
        else: return False
        

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float('-inf'), float('inf'))