# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head
        curNode = head
        prevNode = None
        nextNode = curNode.next
        while curNode:
            curNode.next = prevNode
            prevNode = curNode
            curNode = nextNode
            if nextNode:
                nextNode = nextNode.next
        return prevNode

    def reorderList(self, head: Optional[ListNode]) -> None:
        # mid order element
        slow = head
        fast = head
        while fast:
            print(slow.val, fast.val)
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                break
            slow = slow.next
            
        # We got the first element
        list1 = head
        list2 = slow
        list2 = self.reverseList(list2)
        head = None
        curr = None
        alternate = False
        while list1 and list2:
            #print(curr.val if curr else None)
            if head is None:
                head = list1
                curr = head
                list1 = list1.next
                alternate = True
            else:
                if alternate:
                    curr.next = list2
                    list2 = list2.next
                    curr = curr.next
                    alternate = False
                    #print(curr.val if curr else None)
                else:
                    curr.next = list1
                    list1 = list1.next
                    curr = curr.next
                    alternate = True

