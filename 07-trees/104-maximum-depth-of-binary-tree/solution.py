# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxDepthRec(root, depth):
            if root is None:
                return depth
            
            maxTempDepth = max(maxDepthRec(root.right, depth + 1), maxDepthRec(root.left, depth + 1))
            return maxTempDepth
        return maxDepthRec(root, 0)


        