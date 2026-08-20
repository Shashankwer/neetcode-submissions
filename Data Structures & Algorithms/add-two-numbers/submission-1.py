# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        currNode = None
        num1 = l1
        num2 = l2
        prev_carry = 0
        while num1 and num2:
            num_sum = (num1.val + num2.val + prev_carry)%10
            prev_carry = (num1.val + num2.val+prev_carry)//10
            if currNode is None:
                currNode = ListNode(num_sum)
                head = currNode
            else:
                currNode.next = ListNode(num_sum)
                currNode = currNode.next
            num1 = num1.next
            num2 = num2.next
        while num1:
            num_sum = (num1.val + prev_carry)%10
            prev_carry =  (num1.val + prev_carry)//10
            if currNode is None:
                currNode = ListNode(num_sum)
                head = currNode
            else:
                currNode.next = ListNode(num_sum)
                currNode = currNode.next
            num1 = num1.next
        while num2:
            num_sum = (num2.val + prev_carry)%10
            prev_carry =  (num2.val + prev_carry)//10
            if currNode is None:
                currNode = ListNode(num_sum)
                head = currNode
            else:
                currNode.next = ListNode(num_sum)
                currNode = currNode.next
            num2 = num2.next
        if prev_carry==1:
            if currNode is None:
                currNode = ListNode(prev_carry)
                head = currNode
            else:
                currNode.next = ListNode(prev_carry)
        return head
