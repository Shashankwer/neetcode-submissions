# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp_node = ListNode(0, head)
        first_node = head
        second_node = temp_node
        for _ in range(n):
            first_node = first_node.next
        while first_node:
            second_node = second_node.next
            first_node = first_node.next
        second_node.next = second_node.next.next
        return temp_node.next
