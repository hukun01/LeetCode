class MaxStack:
    """ Overall time complexity to sort N numbers: O(N^2), because each popMax() takes O(N)
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self._stack and self._stack[-1][1] > x:
            self._stack.append((x, self._stack[-1][1]))
        else:
            self._stack.append((x, x))

    def pop(self):
        """
        :rtype: void
        """
        return self._stack.pop()[0]

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1][0]

    def peekMax(self):
        """
        :rtype: int
        """
        return self._stack[-1][1]

    def popMax(self):
        """
        :rtype: int
        """
        myMax = self.peekMax()
        backup = []
        while self.top() != myMax:
            backup.append(self.pop())
        self.pop()
        for b in reversed(backup):
            self.push(b)
        return myMax

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()