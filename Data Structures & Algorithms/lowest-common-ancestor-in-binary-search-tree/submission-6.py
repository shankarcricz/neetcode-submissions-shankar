# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def lowestCommonAncestor1(self, root, p,q,obj):
        if root is None: return None
        if (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val): obj.append(root)

        if p.val < root.val and q.val < root.val:
            self.lowestCommonAncestor1(root.left,p,q,obj)
        if p.val > root.val and q.val > root.val:
            self.lowestCommonAncestor1(root.right,p,q,obj)

        if (root.val == p.val) or (root.val == q.val):
            if (q.val > root.val) or (p.val > root.val):
                self.lowestCommonAncestor1(root.right,p,q,obj)
            else:
                self.lowestCommonAncestor1(root.left,p,q,obj)
            obj.append(root)
            print(root.val)
        return obj


    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans = self.lowestCommonAncestor1(root, p, q, [])
        return ans[-1]
        
            
        
        
        
        

        