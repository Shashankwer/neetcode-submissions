class Node:
    def __init__(self, key:int, val:int):
        self.key = key
        self.value = val
        self.nxt = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.nxt = self.right
        self.right.prev = self.left
    
    def _remove(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt = nxt
        nxt.prev = prev 

    def _add(self, node):
        prev, nxt = self.right.prev, self.right
        prev.nxt = node
        nxt.prev = node
        node.nxt = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._add(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._add(self.cache[key])
        if len(self.cache) > self.capacity:
            node = self.left.nxt
            self._remove(node)
            del self.cache[node.key]

