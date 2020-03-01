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

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.data = nestedList
        self.pos = 0
        self.nestedIter = None

    def next(self):
        """
        :rtype: int
        """
        if self.nestedIter:
            return self.nestedIter.next()
        else:
            val = self.data[self.pos].getInteger()
            self.pos += 1
            return val
        
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.nestedIter and self.nestedIter.hasNext():
            return True
        self.nestedIter = None
        if self.pos < len(self.data):
            element = self.data[self.pos]
            if element.isInteger():
                return True
            else:
                self.nestedIter = NestedIterator(element.getList())
                self.pos += 1
                return self.hasNext()
        return False

    '''
    Another style using generators.

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.iter = self.flatten(nestedList)
        self.nextItem = next(self.iter, None)
    
    def flatten(self, items):
        if isinstance(items, list):
            for nestedItem in items:
                for item in self.flatten(nestedItem):
                    yield item
        elif items.isInteger():
            yield items.getInteger()
        else:
            for item in self.flatten(items.getList()):
                yield item

    def next(self):
        """
        :rtype: int
        """
        currItem = self.nextItem
        self.nextItem = next(self.iter, None)
        return currItem
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.nextItem is not None
    '''
        
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())