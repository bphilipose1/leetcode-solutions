# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDim = 0
        def dim(root):
            if not root:
                return -1  # Return -1 because we count edges, not nodes
            leftHeight = dim(root.left)
            rightHeight = dim(root.right)
            
            self.maxDim = max(self.maxDim, leftHeight + rightHeight + 2)

            return 1 + max(leftHeight, rightHeight)
        dim(root)
        return self.maxDim
        