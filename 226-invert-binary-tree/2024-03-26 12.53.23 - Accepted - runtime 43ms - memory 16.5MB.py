# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def recursiveSwap(root):
            if root is None:
                return None
            
            root.left, root.right = root.right, root.left

            recursiveSwap(root.left)
            recursiveSwap(root.right)

            return root
        return recursiveSwap(root)