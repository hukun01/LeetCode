# 295. Find Median from Data Stream
class MedianFinder:
    '''
    Use two heaps, one storing the smaller half of the data stream,
    another storing the larger half of the data stream, and the median is either on
    one side, or the average of both sides.
    
    Since in Python the heap is min heap, we need to flip the number when pusing numbers
    into small heap, and need to flip it back when using it.
    '''
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heaps = [], []

    def addNum(self, num: int) -> None:
        small, large = self.heaps
        
        # Flip the number to make the largest one become the smallest;
        # Always add to small heap first, and balance the size of two heaps,
        # making sure that len(large) >= len(small)
        heappush(large, num)
        cur_min = heappop(large)
        heappush(small, -cur_min)
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self) -> float:
        small, large = self.heaps
        if len(large) > len(small):
            return large[0]
        else:
            # remember to flip it back
            return (-small[0] + large[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()