# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        temp_queue = collections.deque()
        temp_queue.append(root)

        while temp_queue:
            qLen = len(temp_queue)
            level = []
            #go through the values in the queue at current state (only current level nodes per while loop)
            for x in range(qLen):
                node = temp_queue.popleft()
                #if node is not null
                if node:
                    level.append(node.val)
                    temp_queue.append(node.left)
                    temp_queue.append(node.right)
            if level:
                result.append(level)
        return result

        