# 1188. Design Bounded Blocking Queue
from threading import Lock
class BoundedBlockingQueue(object):
    '''
    Threading.
    Use two locks, one for enqueue, one for dequeue, to ensure each operation
    is synchronized.

    In enqueue(), whenever the queue size == capacity, we can't release the
    en_lock, because the queue is full; otherwise we can release in this
    method. In dequeue(), we can release en_lock if it's locked, because we
    just removed one element.
    Similar logic applies to the de_lock in enqueue() and dequeue().

    Note that we want to lock the de_lock initially, because the queue starts
    empty.
    '''

    def __init__(self, capacity: int):
        self.en_lock = Lock()
        self.de_lock = Lock()
        self.de_lock.acquire()
        self.q = deque()
        self.capacity = capacity

    def enqueue(self, element: int) -> None:
        self.en_lock.acquire()
        self.q.appendleft(element)
        if self.size() < self.capacity:
            self.en_lock.release()

        if self.de_lock.locked():
            self.de_lock.release()


    def dequeue(self) -> int:
        self.de_lock.acquire()
        val = self.q.pop()
        if self.size() > 0:
            self.de_lock.release()

        if self.en_lock.locked():
            self.en_lock.release()

        return val


    def size(self) -> int:
        return len(self.q)