class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _addToHead(self, node):
        cachedNext = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = cachedNext
        cachedNext.prev = node
        self.dict[node.key] = node
    
    def _remove(self, node):
        if node.key not in self.dict:
            return
        
        del self.dict[node.key]
        cachedPrev = node.prev
        cachedNext = node.next
        cachedPrev.next = cachedNext
        cachedNext.prev = cachedPrev
        
    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self._remove(node)
            self._addToHead(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            self._remove(node)
            
        self._addToHead(Node(key, value))
        
        if len(self.dict) > self.capacity:
            self._remove(self.tail.prev)
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)