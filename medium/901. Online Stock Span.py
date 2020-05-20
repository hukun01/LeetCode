# 901. Online Stock Span
class StockSpanner:
    '''
    Monotonic stack.
    Keep the tuple (price, span) in the stack, when seeing a
    new price, pop out all less-or-equal price tuples and add
    up all the spans.
    '''

    def __init__(self):
        self.stack = []

    def next(self, price):
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)