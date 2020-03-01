class TimeMap:
    '''
    Use two dict to store timestamp and values separately,
    keep appending timestamp and value in set().
    In get(), just binary search the upper bound of the target timestamp in times,
    and use the index to look up values.
    '''

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.times = collections.defaultdict(list)
        self.values = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        idx = self.findLowerBound(self.times[key], timestamp)
        if idx - 1 >= 0:
            return self.values[key][idx - 1]
        return ""
        
    def findLowerBound(self, times, target):
        l, h = 0, len(times)
        while l < h:
            m = (l + h) // 2
            if times[m] <= target:
                l = m + 1
            else:
                h = m
        return l

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)