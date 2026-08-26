# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle of the list
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse second half
        second = slow.next
        previous = slow.next = None

        while second:
            backup = second.next
            second.next = previous
            previous = second
            second = backup
        
        # Merge two halves
        first, second = head, previous

        while second:
            firstBackup, secondBackup = first.next, second.next
            first.next = second
            second.next = firstBackup
            first = firstBackup
            second = secondBackup



