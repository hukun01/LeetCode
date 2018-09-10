class MinStack:
    def __init__(self):
        """
        initialize your data structure here.

        Use two stacks, one storing the actual values, another store the running min.
        """
        self._valStack = []
        self._minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._valStack.append(x)
        if self._minStack and self._minStack[-1] < x:
            self._minStack.append(self._minStack[-1])
        else:
            self._minStack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self._valStack.pop()
        self._minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self._valStack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self._minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()