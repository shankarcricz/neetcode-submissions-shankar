# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        matrix = []
        arr=[root]
        while len(arr)>0:
            p=[]
            temp= []

            for r in arr:
                p.append(r.val)
                if r.left:temp.append(r.left)
                if r.right: temp.append(r.right)
            matrix.append(p)
            arr = temp
        print(matrix)
        return matrix[-1][0]

                

             
        
            

            

            
