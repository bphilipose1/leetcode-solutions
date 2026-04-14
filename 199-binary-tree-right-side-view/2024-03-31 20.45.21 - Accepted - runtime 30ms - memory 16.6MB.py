# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        arrayView = []
        q = collections.deque()
        q.append(root)
        while q:
            level = []
            lenQ = len(q)
            for x in range(lenQ):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                    
            if level:
                arrayView.append(level)

        result = []
        for x in arrayView:
            result.append(x[-1])
        return result
            
        