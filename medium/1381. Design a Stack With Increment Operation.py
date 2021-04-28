# 1381. Design a Stack With Increment Operation
class CustomStack:
    '''
    Push and pop operations are O(1) time.

    O(n) time increment is trivial.

    To do O(1) increment, let inc[i] be the added value from stack[0] to
    stack[i]. When poping out an element, add inc[i] to it, and, add inc[i]
    to inc[i - 1] to propagate the added value to the next pop. This is
    similar to the difference array technique where we propagate the difference
    to accumulate the updates.
    '''

    def __init__(self, maxSize: int):
        self.m = maxSize
        self.stack = []
        self.inc = [0] * maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.m:
            self.stack.append(x)

    def pop(self) -> int:
        i = len(self.stack) - 1
        if i < 0:
            return -1
        inc = self.inc[i]
        self.inc[i] = 0
        if i > 0:
            self.inc[i - 1] += inc
        return self.stack.pop() + inc

    def increment(self, k: int, val: int) -> None:
        i = min(k, len(self.stack)) - 1
        if i >= 0:
            self.inc[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)