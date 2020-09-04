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
        self.buf4 = [''] * 4
        self.buf4_len = 0
        self.buf4_idx = 0

    def read(self, buf: List[str], n: int) -> int:
        cur_idx = 0
        while cur_idx < n:
            if self.buf4_len == 0:
                self.buf4_len = read4(self.buf4)
            if self.buf4_len == 0:
                break
            while cur_idx < n and self.buf4_idx < self.buf4_len:
                buf[cur_idx] = self.buf4[self.buf4_idx]
                cur_idx += 1
                self.buf4_idx += 1
            if self.buf4_idx == self.buf4_len:
                self.buf4_idx = 0
                self.buf4_len = 0
        return cur_idx