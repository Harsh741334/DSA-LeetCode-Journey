# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if root.left == None and root.right == None:
            return True
        else:

            def t(p,q):
                if p == None and q == None:
                    return True

                if p and q == None:
                    return False
                if p == None and q:
                    return False
                if p.val != q.val:
                    return False
               

                return t(p.left,q.right) and t(p.right,q.left)
            return t(root.left,root.right)