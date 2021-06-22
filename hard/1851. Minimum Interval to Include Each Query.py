# 1851. Minimum Interval to Include Each Query
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        '''
        Greedy + heap.

        We sort intervals in decreasing order and take them from the end.

        Keep a min heap of (size, end) that we have processed, 'availables'.

        Process each query from small to big. For each query q, update the
        'availables' to remove the minimum (size, end) if end < q.
        Note that when removing things from heap, we use lazy deletion, similar
        to 480. Sliding Window Median.

        Then take out the current interval if its start <= q, and if its
        end >= q, we add the (size, end) to the 'availables' heap.

        Now if there's anything in availables, that's answer for query q.

        One small trick is to use a set to dedup queries, it's not done here.

        Time: O(Q log(Q) + N log(N) + Q log(N)) where Q is len(queries), N is
            len(intervals).
        Space: O(Q + N)
        '''
        intervals.sort(reverse=True)
        availables = []
        ans = [-1] * len(queries)
        for q_i, query in sorted(enumerate(queries), key=lambda q: q[1]):
            while availables and availables[0][1] < query:
                heappop(availables)
            while intervals and intervals[-1][0] <= query:
                start, end = intervals.pop()
                if end >= query:
                    heappush(availables, [end - start + 1, end])
            if availables:
                ans[q_i] = availables[0][0]

        return ans