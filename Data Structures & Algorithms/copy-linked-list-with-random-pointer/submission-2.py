"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        node_copy = {} # map for the node copy made; Allows easy linkages
        currNode = head
        while currNode:
            node_copy[currNode] = Node(currNode.val, None, None)
            currNode = currNode.next
        newHead = None
        newCurrHead = None
        currNode = head
        while currNode:
            newCurrHead = node_copy[currNode]
            if currNode.next:
                newCurrHead.next = node_copy[currNode.next]
            if currNode.random:
                newCurrHead.random = node_copy[currNode.random]
            if newHead is None:
                newHead = newCurrHead
            currNode = currNode.next
        return newHead

