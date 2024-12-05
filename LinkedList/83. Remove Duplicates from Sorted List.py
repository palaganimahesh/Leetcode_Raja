class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def deleteDuplicates(self,head: ListNode) -> ListNode:
        # Edge case: If the list is empty or has only one node
        if not head or not head.next:
            return head

        current = head
        while current and current.next:
            if current.val == current.next.val:
                # Skip the duplicate node
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next

        return head
