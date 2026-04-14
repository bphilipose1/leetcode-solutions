# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        #1. Set head, mid, tail pointers
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #2. Reverse the second half of the linked list
        prev = None
        current = slow.next
        slow.next = None
        while current is not None:
            next_temp = current.next 
            current.next = prev  
            prev = current 
            current = next_temp
            
        
        #4. Combine Lists
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2





        
        