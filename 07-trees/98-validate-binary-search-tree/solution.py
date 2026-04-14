# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #we need to do a in order traversal LNR
        def rec(root, left_val, right_val):
            if not root:
                return True
            
            if not (left_val < root.val < right_val):
                return False
            
            return rec(root.left, left_val, root.val) and rec(root.right, root.val, right_val)
        return rec(root, float('-inf'), float('inf'))
            
            
