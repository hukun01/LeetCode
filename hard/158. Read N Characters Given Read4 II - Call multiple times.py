# 158. Read N Characters Given Read4 II - Call multiple times
# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    '''
    Control flow.
    Use a instance property 'buf4' to be the read4 buffer and store the
    leftover chars.
    '''
    def __init__(self):
        self._reset()

    def _reset(self):
        self.buf4 = [''] * 4
        self.last_i = 0
        self.end = read4(self.buf4)

    def read(self, buf: List[str], n: int) -> int:
        i = 0
        while i < n and self.last_i < self.end:
            if self.last_i < 4:
                buf[i] = self.buf4[self.last_i]
                self.last_i += 1
                i += 1

            if self.last_i == 4:
                self._reset()

        return i