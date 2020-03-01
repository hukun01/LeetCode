class RLEIterator:

    def __init__(self, A: List[int]):
        self.q = A
        self.pos = 0

    def next(self, n: int) -> int:
        while self.pos + 1 < len(self.q) and n > 0:
            times = self.q[self.pos]
            if times >= n:
                self.q[self.pos] -= n
                return self.q[self.pos + 1]
            else:
                self.pos += 2
                n -= times
        return -1


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)