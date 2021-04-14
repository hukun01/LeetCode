# 1348. Tweet Counts Per Frequency
from sortedcontainers import SortedDict
class TweetCounts:
    '''
    1/2 Sorted Dict, (balanced binary search tree).
    A suboptimal solution is to maintain mapping from tweet to frequency list,
    and use bisect to insert the time, but it takes O(n) to insert elements
    into an array.

    Instead, maintain mapping from the tweet to frequency map which is a
    SortedDict (not OrderedDict!). In SortedDict the keys are sorted, so the
    [startTime, endTime] range can be found in O(log) time via irange().

    Time: recordTweet O(1), getTweetCountsPerFrequency O(n), where n is the
          time interval size.
          Note that getTweetCountsPerFrequency also takes log(T) time to find
          the key ranges, where T is the total number of unique times, here
          log(T) is always less than n, because n is at least 60, and T is at
          most 10 ** 9.
    Space: O(M*T) where M is the number of unique tweetName, T is the average
           number of unique times per tweetName.
    '''
    def __init__(self):
        self.data = defaultdict(SortedDict)

    def recordTweet(self, tweetName: str, time: int) -> None:
        tweet_map = self.data[tweetName]
        tweet_map[time] = tweet_map.get(time, 0) + 1

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        interval =  60 if freq == 'minute' else 3600 if freq == 'hour' else 86400
        buckets = [0] * ((endTime - startTime) // interval + 1)
        tweet_map = self.data[tweetName]
        for key in tweet_map.irange(startTime, endTime):
            index = (key - startTime) // interval
            buckets[index] += tweet_map[key]
        return buckets

    '''
    2/2 Segment Tree
    In 1/2, the recordTweet takes O(1) time, getTweetCountsPerFrequency takes
    O(n) time. In this approach we try to trade off recordTweet time to get
    faster getTweetCountsPerFrequency.
    In this segment tree, a tricky part is to insert nodes dynamically as
    needed, because the value space is too wide (10 ** 9) and we don't know it
    beforehand (which means we can't do discretization).

    Time: recordTweet O(log(n)), getTweetCountsPerFrequency O(log(n)), where n
          is the time interval size for the tweetName.
    Space: O(M*T) where M is the number of unique tweetName, T is the average
           number of unique times per tweetName.
    '''

    def __init__(self):
        self.segments = {}
        self.times = {
            'minute': 60,
            'hour': 60 * 60,
            'day': 24 * 60 * 60,
        }

        
    def recordTweet(self, tweetName: str, time: int) -> None:
        if tweetName not in self.segments:
            self.segments[tweetName] = SegTreeNode(0, 10 ** 9 + 5)

        self.segments[tweetName].insert(time)
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if tweetName not in self.segments:
            return []
        
        root = self.segments[tweetName]
        step = self.times[freq]
        ans = []
        for i in range(startTime, endTime+1, step):
            ans.append(SegTreeNode.query_range_sum(root, i, min(endTime, i + step - 1)))
        
        return ans
        

class SegTreeNode:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.left = self.right = None
        self.sum = 0


    def insert(self, p):
        if p == self.a == self.b:
            self.sum += 1
            return

        if not self.a <= p <= self.b:
            return

        m = (self.a + self.b) // 2
        self.left = self.left or SegTreeNode(self.a, m)
        self.right = self.right or SegTreeNode(m+1, self.b)

        self.left.insert(p)
        self.right.insert(p)

        self.sum = self.left.sum + self.right.sum


    @staticmethod
    def query_range_sum(node, a, b):
        if not node or node.a > b or node.b < a:
            return 0

        m = (node.a + node.b) // 2
        if node.a >= a and node.b <= b:
            return node.sum

        return SegTreeNode.query_range_sum(node.left, a, b) + SegTreeNode.query_range_sum(node.right, a, b)


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)