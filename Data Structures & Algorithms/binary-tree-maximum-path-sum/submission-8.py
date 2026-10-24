# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mappy = {}
        def recurse(root):
            if not root: return None
            leftSum = recurse(root.left)
            rightSum = recurse(root.right)
            if leftSum is not None: mappy[leftSum] = 1
            if rightSum is not None: mappy[rightSum] = 1
            if leftSum is None and rightSum is None:
                tot = root.val
                leftSum=0
                rightSum=0
            elif leftSum is None:
                tot = root.val+rightSum
                leftSum=0
            elif rightSum is None:
                tot = root.val+leftSum
                rightSum=0
            else:
                tot = root.val + leftSum + rightSum
            mappy[tot]=1
            returnValue = root.val + max(leftSum,rightSum)
            mappy[root.val]=1
            mappy[returnValue]=1
            return returnValue if returnValue>root.val else root.val


        recurse(root)
       
        return max(mappy)

        