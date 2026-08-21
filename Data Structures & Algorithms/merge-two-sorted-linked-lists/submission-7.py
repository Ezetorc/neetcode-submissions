# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a = list1
        b = list2
        dummy = ListNode(0, a)
        t = dummy

        while a != None and b != None:
            if a.val <= b.val:
                t.next = a
                t = a
                a = a.next
            else:
                t.next = b
                t = b
                b = b.next
        
        if a != None and b == None:
            t.next = a
        elif b != None and a == None:
            t.next = b
        
        return dummy.next


            
