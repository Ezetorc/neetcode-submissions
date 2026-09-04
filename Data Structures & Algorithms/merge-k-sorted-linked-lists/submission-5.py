# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeTwoLists(self, a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy

        while a and b:
            if a.val > b.val:
                node.next = b
                node = b
                b = b.next
            else:
                node.next = a
                node = a
                a = a.next
            
        node.next = a if a else b
            
        return dummy.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            newCollection = []
            index = 0

            while index < len(lists):
                if index + 1 < len(lists):
                    newList = self.mergeTwoLists(lists[index], lists[index + 1])
                    newCollection.append(newList)
                else:
                    newCollection.append(lists[index])
                
                index += 2

            lists = newCollection
        
        return lists[0]









