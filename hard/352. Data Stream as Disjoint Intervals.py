# 352. Data Stream as Disjoint Intervals
from sortedcontainers import SortedList
class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = SortedList()

    def addNum(self, val: int) -> None:
        # find the next inerstion point, e.g., get 1 in [[1,3]] when inserting 1.
        insert_pos = self.intervals.bisect_right([val, math.inf])
        
        if insert_pos == 0:
            # self.intervals is either empty, or val is too small
            if self.intervals and self.intervals[0][0] <= val + 1:
                self.intervals[0][0] = val
            else:
                self.intervals.add([val, val])
        else:
            # check for left merge, if no merge, we add the [val, val]
            left = insert_pos - 1
            if self.intervals[left][1] + 1 >= val:
                self.intervals[left][1] = max(self.intervals[left][1], val)
                right = insert_pos
            else:
                self.intervals.add([val, val])
                left = insert_pos # now the left is the added interval
                right = insert_pos + 1
            # now check whether to merge left and right
            if right < len(self.intervals):
                if self.intervals[right][0] - 1 <= val:
                    self.intervals[right][0] = val
                if self.intervals[left][1] >= self.intervals[right][0]:
                    self.intervals[left][1] = max(self.intervals[left][1], self.intervals[right][1])
                    self.intervals.pop(right)

    def getIntervals(self) -> List[List[int]]:
        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()