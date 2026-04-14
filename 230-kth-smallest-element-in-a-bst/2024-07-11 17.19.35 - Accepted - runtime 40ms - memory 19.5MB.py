# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #in order traversal, and store each node value in an array
        # index the kth element
        temp_arr = []
        def recursive_func(root):
            #LNR for InOrder Traversal
            if root is None:
                return
            recursive_func(root.left)
            temp_arr.append(root.val)
            recursive_func(root.right)
        
        recursive_func(root)
        return temp_arr[k-1]
            
