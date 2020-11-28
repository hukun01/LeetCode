# 1670. Design Front Middle Back Queue
class FrontMiddleBackQueue:
    '''
    Deque.
    Three keys:
    1. Notice that there will be either 0 or one middle value, because once
       there are 2 middle values, we will distribute them to front and back.
       Hence, only maintaining two halves of the list is sufficient.
    2. When there's 1 middle value and we are adding another, as we need to
       add the new one in front of the existing value, we need to check which
       half is longer, if front is longer (exactly one more), we move the tail
       of front to the head of back, and append the new middle to the front.
       This part is similar to 295. Find Median from Data Stream
    3. To make it clean to find middle, when splitting the list into two
       halves, we keep the front equal to or longer than back, and based on #2
       where we always append the new middle to the front, we can always check
       front when poping middle values.
    '''
    def __init__(self):
        self.front = deque()
        self.back = deque()

    def pushFront(self, val: int) -> None:
        self.front.appendleft(val)
        self._balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.front) > len(self.back):
            self.back.appendleft(self.front.pop())
        self.front.append(val)
        self._balance()

    def pushBack(self, val: int) -> None:
        self.back.append(val)
        self._balance()

    def popFront(self) -> int:
        val = self.front.popleft() if self.front else -1
        self._balance()
        return val

    def popMiddle(self) -> int:
        val = (self.front or [-1]).pop()
        self._balance()
        return val

    def popBack(self) -> int:
        val = (self.back or self.front or [-1]).pop()
        self._balance()
        return val

    def _balance(self):
        '''
        Keep len(self.front) >= len(self.back)
        '''
        while len(self.front) < len(self.back):
            self.front.append(self.back.popleft())
        while len(self.front) > len(self.back) + 1:
            self.back.appendleft(self.front.pop())

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()