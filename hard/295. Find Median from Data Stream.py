# 295. Find Median from Data Stream
class MedianFinder:
    '''
    Use two heaps, one storing the smaller half of the data stream,
    another storing the larger half of the data stream, and the median is
    either on one side, or the average of both sides.
    
    Since in Python the heap is min heap, we need to flip the number when
    pusing numbers into small heap, and need to flip it back when using it.
    '''
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heaps = [], []

    def addNum(self, num: int) -> None:
        small, large = self.heaps

        # We keep an invariant: len(large) >= len(small), and the diff <= 1.
        # To ensure 'large' always has larger numbers, we add new numbers to
        # 'large' first, then pop the (potentially updated) cur_min and add it
        # to the 'small'. This way we ensure all numbers in 'small' <= that in
        # 'large'.
        # 
        # Now len(large) <= len(small), to keep our invariant, we need to
        # balance the size of two heaps. After the above operation, if
        # len(large) < len(small), we move the largest number from 'small' to
        # 'large'; otherwise, we know len(large) == len(small).
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