# 1286. Iterator for Combination
class CombinationIterator:
    '''
    This is a natual recursion problem, but to make an iterator for it, we can
    convert it to a step-by-step iteration, so we can exit and resume freely.

    Use a recursion -> iteration template. Write the recursion function first,
    mark all the entry points. For each entry point, we need to push that to
    the stack, after gathering all context parameters.
    '''

    def __init__(self, characters: str, combinationLength: int):
        self.arr = characters
        self.k = combinationLength
        self.stack = [(0, 0, 0, [])] # (entry, start, i, path)
        self.next_comb = None
        self.move_to_next()

    '''
    Below step() is based on this perm recursion.
        def perm(self, path, start):
            # entry_point_0
            if len(path) == k:
                do_something(''.join(path))
                return
            for i in range(start, len(arr)):
                path.append(arr[i])
                self.perm(arr, path, i + 1)
                # entry_point_1
                path.pop()                            
    '''
    def step(self) -> str:
        entry, start, i, path = self.stack.pop()
        if entry == 0:
            if len(path) == self.k:
                return ''.join(path)
            i = start
        elif entry == 1:
            path.pop()

        if i == len(self.arr):
            return        # for-loop in perm() finishes

        path.append(self.arr[i])
        # save the current context before entering the recursion, so we can resume later,
        # the entry here should be the current entry.
        self.stack.append((1, start, i + 1, path))
        # this is to start a fresh recursion, the entry should be the first entry.
        # this needs to be at the top of the stack as it needs to run immediately.
        self.stack.append((0, i + 1, i + 1, path))
    
    def move_to_next(self) -> str:
        while len(self.stack) > 0:
            self.next_comb = self.step()
            if self.next_comb is not None:
                break

    def next(self) -> str:
        curr_comb = self.next_comb
        self.move_to_next()
        return curr_comb

    def hasNext(self) -> bool:
        return self.next_comb is not None
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()