class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.dict = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _addToHead(self, node):
        cachedNext = self.head.next
        self.head.next = node
        node.prev = self.head
        cachedNext.prev = node
        node.next = cachedNext
        self.dict[node.key] = node

    def _remove(self, key):
        if key not in self.dict:
            return
        node = self.dict[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        self.dict.pop(key)

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        value = self.dict[key].val
        self._remove(key)
        self._addToHead(Node(key, value))
        return value
        
    def put(self, key: int, value: int) -> None:
        if key not in self.dict:
            if len(self.dict) == self.c:
                self._remove(self.tail.prev.key)
        else:
            self._remove(key)
            
        self._addToHead(Node(key, value))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)