# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge_two_list(self, list1,list2):
        result = None
        curr = None
        while list1 and list2:
            if list1.val < list2.val:
                if result is None:
                    result = list1
                    curr = result
                else:
                    curr.next = list1
                    curr = curr.next
                list1 = list1.next
            else:
                if result is None:
                    result = list2
                    curr = result
                else:
                    curr.next = list2
                    curr = curr.next
                list2 = list2.next
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        return result


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        print(len(lists))
        if len(lists)<2:
            if len(lists) == 0:
                return None
            else:
                return lists[0]
        for i in range(1, len(lists)):
            lists[0] = self.merge_two_list(lists[0],lists[i])
        return lists[0]