class ZigzagIterator:
  '''
  This solution handles any number of vectors.
  The idea is to simply prefetch the next values from each vector, because
  Python doesn't have a hasNext() method for iterators.
  '''
    def __init__(self, v1: List[int], v2: List[int]):
        it1 = iter(v1)
        it2 = iter(v2)
        self.data = [(it1, next(it1, None)), (it2, next(it2, None))]
        self.idx = 0

    def next(self) -> int:
        value = None
        while value is None:
            it, value = self.data[self.idx]
            self.data[self.idx] = (it, next(it, None))
            self.idx = (self.idx + 1) % len(self.data)
        return value

    def hasNext(self) -> bool:
        return any(value is not None for _, value in self.data)
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
