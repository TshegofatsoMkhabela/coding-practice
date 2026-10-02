# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        head_of_list = ListNode()
        current_node = head_of_list

        def merge(current_node, list1, list2):
            if not list1: 
                current_node.next = list2
                return
            if not list2: 
                current_node.next = list1
                return

            if list1.val < list2.val:
                current_node.next = list1
                list1 = list1.next
            else:
                current_node.next = list2
                list2 = list2.next
            
            current_node = current_node.next
            
            return merge(sorted, list1, list2)
        
        merge(current_node, list1, list2)
        return head_of_list.next
        