# 232. Implement Queue using Stacks
class MyQueue:
    '''
    Use two stacks, one to store incoming elements, another to store outgoing elements.
    And have a moveData method that pops out all incoming stack's data to outgoing stack.
    That way the amortized time complexity is O(1).
    
    The application for this implementation is to separate read & write of a queue in
    multi-thread environment. One of the stacks is for read, and another is for write.
    They only interfere each other when the former one is full or latter is empty.
    As long as the second stack is not empty, push operation (enqueue) will not lock the
    second stack for pop (dequeue).
    '''

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.incoming, self.outgoing = [], []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.incoming.append(x)
    
    def moveData(self) -> None:
        if not self.outgoing:
            while self.incoming:
                self.outgoing.append(self.incoming.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.moveData()
        return self.outgoing.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.moveData()
        return self.outgoing[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.incoming) == len(self.outgoing) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()