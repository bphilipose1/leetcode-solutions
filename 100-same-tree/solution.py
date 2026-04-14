# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def recCheck(node1, node2):
            if node1 == None and node2 == None:
                return True
            elif node1 != None and node2 != None and recCheck(node1.left, node2.left) and recCheck(node1.right, node2.right):
                if node1.val == node2.val:
                    return True
                else:
                    return False

            else:
                return False
        return recCheck(p, q)