# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prevNode = None
        curNode = head
        nextNode = head.next
        while curNode:
            curNode.next = prevNode
            prevNode = ListNode(curNode.val, curNode.next)
            if nextNode:
                curNode = ListNode(nextNode.val, nextNode.next)
                nextNode = nextNode.next
            else:
                curNode = None
        return prevNode