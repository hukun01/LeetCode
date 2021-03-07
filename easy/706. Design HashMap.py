class Node:

    def __init__(self, key, val=None):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:
    '''
    Use an array to store linked list dummy heads; use linked list to resolve
    key collision.
    Automatically scale up/down based on total node count.
    '''

    _EXPAND_FACTOR = 1.75
    _EXPAND_THRESHOLD = 1.25
    _INITIAL_CAPACITY = 10
    _SHRINKING_FACTOR = 0.5
    _SHRINKING_THRESHOLD = 0.25


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.capacity = MyHashMap._INITIAL_CAPACITY
        self.entries = [Node(i) for i in range(self.capacity)]
        self.hash_base = 1337
        self.total_nodes = 0


    def _build_key(self, key):
        return key % self.hash_base % self.capacity


    def _extend_capacity(self):
        self.capacity = int(MyHashMap._EXPAND_FACTOR * self.capacity)

        self._resize()


    def _resize(self):
        new = [Node(i) for i in range(self.capacity)]
        for node in self.entries:
            while node.next:
                new_key = self._build_key(node.next.key)
                tail = new[new_key]
                while tail.next:
                    tail = tail.next
                tail.next = node.next
                cache = node.next
                node.next = None
                node = cache
        
        self.entries = new


    def _shrink_capacity(self):
        self.capacity = max(
            MyHashMap._INITIAL_CAPACITY,
            int(MyHashMap._SHRINKING_FACTOR * self.capacity))
        
        self._resize()


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        internal_key = self._build_key(key)
        tail = self.entries[internal_key]
        while tail.next:
            if tail.next.key == key:
                tail.next.val = value
                return
            tail = tail.next

        node = Node(key, value)
        tail.next = node
        self.total_nodes += 1
        if self.total_nodes > self.capacity * MyHashMap._EXPAND_THRESHOLD:
            self._extend_capacity()


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        internal_key = self._build_key(key)
        tail = self.entries[internal_key]
        while tail.next:
            if tail.next.key == key:
                return tail.next.val
            tail = tail.next
        return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        internal_key = self._build_key(key)
        tail = self.entries[internal_key]
        while tail.next and tail.next.key != key:
            tail = tail.next
        if tail.next:
            pre = tail
            cur = tail.next
            pre.next = cur.next
            self.total_nodes -= 1

        if self.total_nodes < self.capacity * MyHashMap._SHRINKING_THRESHOLD:
            self._shrink_capacity()


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)