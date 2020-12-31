# 460. LFU Cache
class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        self.freq = 1

class DoublelyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node() # nodes closer to tail is older
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def prepend(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

        self.size += 1

    def remove_node(self, node):
        if self.size == 0:
            return None

        node.prev.next = node.next
        node.next.prev = node.prev

        self.size -= 1
        return node

    def remove_eldest(self):
        return self.remove_node(self.tail.prev)


class LFUCache:
    '''
    Frequency to doubly linked list of nodes.
    Overall, similar to 146. LRU Cache. To achieve O(1) get() and put(), we
    use a mapping to track key frequency and the list of nodes ordered by
    their original sequence. The nodes are FIFO when expiring.

    One key is to track the min frequency, and increment it when there's no
    nodes with this min frequency. And when a new node is added, reset min
    frequency to 1.
    '''

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key2node = dict()
        self.freq2list = defaultdict(DoublelyLinkedList)
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key2node:
            return -1

        node = self.key2node[key]
        self._update_node_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key not in self.key2node:
            if len(self.key2node) == self.capacity:
                removed = self.freq2list[self.min_freq].remove_eldest()
                self.key2node.pop(removed.key)

            node = Node(key, value)
            self.freq2list[1].prepend(node)
            self.min_freq = 1
        else:
            node = self.key2node[key]
            node.val = value
            self._update_node_freq(node)

        self.key2node[key] = node


    def _update_node_freq(self, node: Node):
        freq_list = self.freq2list[node.freq]
        freq_list.remove_node(node)

        if self.min_freq == node.freq and freq_list.size == 0:
            self.min_freq += 1

        node.freq += 1
        self.freq2list[node.freq].prepend(node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)