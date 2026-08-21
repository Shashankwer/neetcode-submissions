class MyHashMap:

    def __init__(self):
        self.internal_map = []

    def put(self, key: int, value: int) -> None:
        index = self.get_key_index(key)
        if index!=-1:
            self.internal_map[index] = [key, value]
        else:
            self.internal_map.append([key, value])

    def get(self, key: int) -> int:
        index = self.get_key_index(key)
        if index == -1:
            return -1
        else:
            return self.internal_map[index][1]

    def remove(self, key: int) -> None:
        index = self.get_key_index(key)
        if index !=-1:
            self.internal_map.pop(index)

    def get_key_index(self, key: int) -> None:
        for index,[k, v] in enumerate(self.internal_map):
            if key == k:
                return index
        return -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)