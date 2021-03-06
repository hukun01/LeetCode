# 1115. Print FooBar Alternately
from threading import Lock
class FooBar:
    def __init__(self, n):
        self.n = n
        self.fooLock = Lock()
        self.barLock = Lock()
        self.barLock.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            if self.fooLock.acquire():
                # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()
                self.barLock.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            if self.barLock.acquire():
                # printBar() outputs "foo". Do not change or remove this line.
                printBar()
                self.fooLock.release()