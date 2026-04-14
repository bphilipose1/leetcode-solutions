"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldCopy = {None:None}

        curr = head
        while curr:
            tempNode = Node(curr.val)
            oldCopy[curr] = tempNode
            curr = curr.next
        
        curr = head
        while curr:
            copyNode = oldCopy[curr]
            copyNode.random = oldCopy[curr.random]
            copyNode.next = oldCopy[curr.next]
            curr = curr.next
        return oldCopy[head]