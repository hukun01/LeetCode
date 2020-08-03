# 341. Flatten Nested List Iterator
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
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

    def __init__(self, nestedList: [NestedInteger]):
        self.data = nestedList
        self.pos = 0
        self.nested_iter = None

    def next(self) -> int:
        if self.nested_iter:
            return self.nested_iter.next()
        else:
            val = self.data[self.pos].getInteger()
            self.pos += 1
            return val

    def hasNext(self) -> bool:
        if self.nested_iter and self.nested_iter.hasNext():
            return True
        self.nested_iter = None
        if self.pos < len(self.data):
            element = self.data[self.pos]
            if element.isInteger():
                return True
            else:
                self.nested_iter = NestedIterator(element.getList())
                self.pos += 1
                return self.hasNext()
        return False

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