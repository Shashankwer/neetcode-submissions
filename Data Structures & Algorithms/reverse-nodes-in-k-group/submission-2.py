# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isSubSetList(self,node: Optional[ListNode], k:int) -> Optional[ListNode]:
        currNode = node
        for _ in range(k):
            if not currNode:
                return None
            currNode = currNode.next
        return currNode

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # sample a batch of k nodes and reverse the list and link them together.       
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            nextSubset = self.isSubSetList(groupPrev,k)
            if not nextSubset:
                break
            print(nextSubset.val)
            groupNext = nextSubset.next
            prev, curr = nextSubset.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp 
            tmp = groupPrev.next
            groupPrev.next = nextSubset
            groupPrev = tmp
        return dummy.next

        
            


