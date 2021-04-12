# 1348. Tweet Counts Per Frequency
from sortedcontainers import SortedDict
class TweetCounts:
    '''
    Balanced binary search tree.
    A suboptimal solution is to maintain mapping from tweet to frequency list,
    and use bisect to insert the time, but it takes O(n) to insert elements
    into an array.

    Instead, maintain mapping from the tweet to frequency map which is a
    SortedDict (not OrderedDict!). In SortedDict the keys are sorted, so the
    [startTime, endTime] range can be found in logN time via irange().
    getTweetCountsPerFrequency() takes O(n) time.
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


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)