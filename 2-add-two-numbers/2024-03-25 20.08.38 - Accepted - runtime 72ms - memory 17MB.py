# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        carry = 0
        curr = head

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            tempTotal = val1 + val2 + carry
            print(tempTotal)
            if tempTotal > 9:
                out = tempTotal % 10
                carry = tempTotal // 10
            else:
                carry = 0
                out = tempTotal
            print(carry, out)
            curr.next = ListNode(0)
            curr = curr.next
            curr.val = out

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head.next
