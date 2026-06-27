# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def t(l,r):
            if l == None and r == None:
                return True

            if l and r == None:
                return False
            if l == None and r:
                return False
            if l.val != r.val:
                return False

            return t(l.left,r.left) and t(l.right,r.right)
        return t(p,q)
        
        
            

        

        
