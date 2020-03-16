# 1381. Design a Stack With Increment Operation
class CustomStack:
    '''
    Push and pop operations are O(1) time.
    
    O(n) time increment is trivial.
    
    To do O(1) increment, use an array inc to record the
    latest diff that needs to be added upon pop.
    inc[i] means from stack[0] to stack[i], all values need
    to be incremented by inc[i].
    
    Also, add inc[i] to inc[i - 1] for the next pop.
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