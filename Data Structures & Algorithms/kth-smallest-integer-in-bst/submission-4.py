# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        array = []

        def helper(root):
            if not root: return
            helper(root.left)
            array.append(root.val)
            helper(root.right)
        helper(root)
        if len(array)>=k: return array[k-1]
        else: 0


        