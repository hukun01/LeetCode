# 341. Flatten Nested List Iterator
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    '''
    Recursive structure to handle recursive data.
    '''
    def __init__(self, nestedList: [NestedInteger]):
        self.list_iter = iter(nestedList) # traverse top level nested list.
        self.curr_int = None
        self.curr_iter = None # recursively traverse each NestedInteger.
    
    def next(self) -> int:
        val = self.curr_int
        self.curr_int = None
        return val
    
    def hasNext(self) -> bool:
        if self.curr_int is not None:
            return True
        if self.curr_iter and self.curr_iter.hasNext():
            self.curr_int = self.curr_iter.next()
            return True

        next_val = next(self.list_iter, None)
        if next_val is None:
            return False
        if next_val.isInteger():
            self.curr_int = next_val.getInteger()
        else:
            self.curr_iter = NestedIterator(next_val.getList())
        return self.hasNext()
    
    '''
    Something that works but less elegant.
    '''

class NestedIterator:

    def __init__(self, nestedList: [NestedInteger]):
        self.idx = 0
        self.data = nestedList
        self.val = None
        self.nested_iter = None


    def _populate(self):
        if self.val is not None:
            return

        if self.nested_iter is not None and self.nested_iter.hasNext():
            self.val = self.nested_iter.next()
            return

        if self.idx < len(self.data):
            cur = self.data[self.idx]
            self.idx += 1
            if cur.isInteger():
                self.val = cur
            else:
                self.nested_iter = NestedIterator(cur.getList())
                self._populate()


    def next(self) -> int:
        self._populate()
        ans = self.val
        self.val = None
        return ans


    def hasNext(self) -> bool:
        self._populate()
        return self.val is not None

    '''
    Another style using generators.
    '''
    def __init__(self, nestedList: [NestedInteger]):
        self.iter = self.flatten(nestedList)
        self.nextItem = next(self.iter, None)
    
    def flatten(self, items):
        if isinstance(items, list):
            for nestedItem in items:
                yield from self.flatten(nestedItem)
        elif items.isInteger():
            yield items.getInteger()
        else:
            yield from self.flatten(items.getList())

    def next(self) -> int:
        currItem = self.nextItem
        self.nextItem = next(self.iter, None)
        return currItem

    def hasNext(self) -> bool:
        return self.nextItem is not None
        
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())