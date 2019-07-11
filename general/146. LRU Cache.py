class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _addToHead(self, node):
        self.nodes[node.key] = node
        
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        
    def _remove(self, node: Node):
        self.nodes.pop(node.key)
        node.next.prev = node.prev
        node.prev.next = node.next

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self._remove(node)
        self._addToHead(node)
        return node.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self._remove(self.nodes[key])
        elif len(self.nodes) == self.capacity:
            self._remove(self.tail.prev)

        self._addToHead(Node(key, value))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)