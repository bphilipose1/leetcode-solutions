# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Step 1: Flatten all nlinked lists into a signle array
        all_values = []
        for linked_list in lists:
            while linked_list:
                all_values.append(linked_list.val)
                linked_list = linked_list.next

        # Step 2: Heapify the array
        heapq.heapify(all_values)

        # Step:3 Build the resulting sorted linkedlist
        dummy = ListNode(0)  # Dummy node to simplify list construction
        current = dummy
        
        while all_values:
            smallest = heapq.heappop(all_values)
            current.next = ListNode(smallest)
            current = current.next
        
        return dummy.next