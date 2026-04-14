# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def recursiveCheck(root1, root2):
            if root1 is None or root2 is None:
                #check if they both are none, to show that they are exactly the same
                if root1 is None and root2 is None: 
                    print("True")
                    return True
            if root1 is not None and root2 is not None and recursiveCheck(root1.right, root2.right) and recursiveCheck(root1.left, root2.left) and root1.val == root2.val:
                print("True")
                return True
            else:
                print("False")
                return False
        def recursiveSearch(root1, root2):
            if root1 is None:
                return False
            if root1.val == root2.val:
                
                return recursiveCheck(root1, root2)

            #see if you can find node to match root in other subtrees
            return recursiveSearch(root1.left, root2) or recursiveSearch(root1.right, root2)
        return recursiveSearch(root, subRoot)








                