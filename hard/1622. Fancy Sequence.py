# 1622. Fancy Sequence
class Fancy:

    def __init__(self):
        '''
        Array.
        If we have this sequence of operations:
        append x0, addAll y0, multAll z0, append x1, addAll y1, multAll z1.
        We have:
        data: [x0,      x1]
        add:  [y0 * z0, (y0*z0 + y1) * z1]
        mul:  [z0,      z0 * z1]
        Final result should be [((x0 + y0) * z0 + y1) * z1, (x1 + y0 + y1) * z0 * z1]
        Namely [(x0 + y0) * z0 * z1 + y1 * z1, (x1 + y0 + y1) * z0 * z1]
        Then in getIndex(), m = z1, inc = y1 * z1.

        Essentially, we are trying to isolate the added and multiplied parts from
        the data, add, and mul lists.
        '''
        self.data = []
        self.add = [0]
        self.mul = [1]

    def append(self, val: int) -> None:
        self.data.append(val)
        self.add.append(self.add[-1])
        self.mul.append(self.mul[-1])

    def addAll(self, inc: int) -> None:
        self.add[-1] += inc

    def multAll(self, m: int) -> None:
        self.add[-1] *= m
        self.mul[-1] *= m

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.data):
            return -1
        m = self.mul[-1] // self.mul[idx]
        inc = self.add[-1] - self.add[idx] * m
        return (self.data[idx] * m + inc)  % (10 ** 9 + 7)


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)