# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        result = []
        q.append(root)
        while q:
            qLen = len(q)
            level = []
            for x in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            result.append(level)

        fin = []
        for x in result:
            if x:
                fin.append(x[-1])

        return fin
        