# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        listSize = 1
        while temp.next:
            temp = temp.next
            listSize += 1
        print(listSize)
        goalNode = listSize - n
        if goalNode == 0:
            return head.next

        workNode = head
        for _ in range(goalNode-1):
            workNode = workNode.next
        workNode.next = workNode.next.next if workNode.next else None
        return head


