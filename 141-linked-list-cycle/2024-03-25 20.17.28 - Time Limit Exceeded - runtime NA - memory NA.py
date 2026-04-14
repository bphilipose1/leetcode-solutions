# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        curr = head
    
        while curr.next:
            nextNode = curr.next
            if curr.val > nextNode.val:
                return True
            curr = nextNode
        return False

