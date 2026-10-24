# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            c = 0
            map2 = {}
            for i in range(len(inorder)):
                map2[inorder[i]] = i

            def recurse(root, c, currind, lo, hi):
                if c >= len(preorder): return
                c += 1
                if lo < currind and lo <= map2.get(preorder[c]) < currind:
                    root.left = TreeNode(preorder[c])
                    c = recurse(root.left, c, map2.get(preorder[c]), lo, currind - 1)
                if currind < hi and currind < map2.get(preorder[c]) <= hi:
                    root.right = TreeNode(preorder[c])
                    c = recurse(root.right, c, map2.get(preorder[c]), currind + 1, hi)
                return c

            rooty = TreeNode(preorder[c])
            recurse(rooty, 0, map2.get(preorder[c]), 0, len(inorder) - 1)
            return rooty