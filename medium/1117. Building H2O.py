# 1117. Building H2O
from threading import Barrier, Semaphore
class H2O:
    '''
    Threading.

    Learn about Barrier and Semaphore in Python.
    Barrier(x) is a structure that waits for x calls of wait();
    Semaphore(x) is a counter that is available when x > 0, and not available
    when x gets to 0.
    '''

    def __init__(self):
        self.b = Barrier(3)
        self.h = Semaphore(2)
        self.o = Semaphore(1)


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        with self.h:
            self.b.wait()
            releaseHydrogen()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        with self.o:
            self.b.wait()
            releaseOxygen()