# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recusiveCheck(root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is not None and root2 is not None and recusiveCheck(root1.left, root2.left) and recusiveCheck(root1.right, root2.right):
                if root1.val == root2.val:
                    return True
                else:
                    return False
            else:
                return False
        return recusiveCheck(p, q)