# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        head_of_sorted = ListNode()
        sorted = head_of_sorted

        def merge(sorted, list1, list2):
            if not list1: 
                sorted.next = list2
                return
            if not list2: 
                sorted.next = list1
                return

            if list1.val < list2.val:
                sorted.next = list1
                list1 = list1.next
            else:
                sorted.next = list2
                list2 = list2.next
            
            sorted = sorted.next
            
            return merge(sorted, list1, list2)
        
        merge(sorted, list1, list2)
        return head_of_sorted.next
        