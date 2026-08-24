# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        left = list1
        right = list2
        if not left:
            return right
        if not right:
            return left
        head = None
        currNode = None
        while left and right:
            if not head:
                if left.val > right.val:
                    head = right
                    right = right.next
                    head.next = None
                    currNode = head
                else:
                    head = left
                    left = left.next
                    head.next = None
                    currNode = head
            else:
                if left.val > right.val:
                    currNode.next = right
                    right = right.next
                    currNode = currNode.next
                    currNode.next = None
                else:
                    currNode.next = left
                    left = left.next
                    currNode = currNode.next
                    currNode.next = None
        while left:
            currNode.next = left
            left = left.next
            currNode = currNode.next
            currNode.next = None
        while right:
            currNode.next = right
            right = right.next
            currNode = currNode.next
            currNode.next = None
        return head

