# 1206. Design Skiplist
class LinkedNode:

    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.down = None
        self.up = None

    def __repr__(self):  # for debug only
        ans = []
        node = self
        while node:
            ans.append(node.val)
            node = node.next
        return ' '.join([str(c) for c in ans])

class Skiplist:
    '''
    Linked list based data structure.
    Bottom (0-indexed), aka, 0th level has all nodes, and i-th level has more
    nodes than (i-1)th level, based on probability.
    Each horizontal level is a linked list with 'prev' and 'next' pointers on
    each node. Each vertical tower is connected by nodes with the same value
    with 'up' and 'down' pointers. Note that every new list has head and tail
    nodes to handle boundaries and avoid too many null checks, and the new
    list's head's is linked with the previous level's head.

    The critical method to implement is skip_search(), where we start from the
    top of the skiplist, and return the largest node whose value is less than
    or equal to the target.
    Based on skip_search(), we can find the insertion place to add the new
    number, when adding, use a coin-flip like process to determine whether we
    want to add the node to the upper level as well.
    Based on skip_search(), we can find the node to delete, and we delete all
    nodes in the same tower.

    Reference: https://www.ics.uci.edu/~pattis/ICS-23/lectures/notes/Skip%20Lists.pdf
    '''

    def __init__(self):
        self.levels = []
        self.add_new_list()

    def add_new_list(self):
        tail = LinkedNode(inf)
        head = LinkedNode(-inf, next=tail)
        tail.prev = head

        if self.levels:
            prev_head = self.levels[-1]
            prev_head.up = head
            head.down = prev_head

        self.levels.append(head)
    
    def skip_search(self, target):
        p = self.levels[-1] # start from top
        while p.next.val <= target:
            p = p.next
        while p.down:
            p = p.down
            while p.next.val <= target:
                p = p.next
        return p

    def search(self, target: int) -> bool:
        p = self.skip_search(target)

        return p.val == target

    def add(self, num: int) -> None:
        prev = self.skip_search(num)
        down = None
        i = 0
        while True:
            cur = LinkedNode(num)
            self.insert(down, prev, cur)
            should_insert_up = randrange(4) == 0
            if not should_insert_up:
                break
            i += 1
            if i == len(self.levels):
                self.add_new_list()
            while prev.up is None:
                prev = prev.prev
            prev = prev.up
            down = cur

    def insert(self, down, prev, cur):
        cur.prev = prev
        cur.next = prev.next
        prev.next.prev = cur
        prev.next = cur
        if down:
            cur.down = down
            down.up = cur

    def erase(self, num: int) -> bool:
        node = self.skip_search(num)
        if node.val != num:
            return False
        while node:
            prev = node.prev
            prev.next = node.next
            node.next.prev = prev
            node = node.up
        return True


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)