# 1751. Maximum Number of Events That Can Be Attended II
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        '''
        DP.
        Let f[i][j] be the max value from j events from events[:i].
        f[i+1][j] is max of two cases:
            1. f[i][j], when we skip event 'i';
            2. f[p][j-1], where p is the the largest job index that ends before
               event i starts. Same as prev() in 1235, except exclusive here.

        We sort events by end time, this ensures that we check events in
        chronological order.
        Note that we put endTime at front, to enable bisect() to work.
        Also note that we need to search for (start - 1, inf) tuple, in order
        to locate the latest job that ends at the first 'start', so the whole
        'bisect() - 1' would be the latest job that ends exclusively before
        'start'.

        Time: O(n log(n) + kn), for sort() and DP loop.
        Space: O(kn)

        Similar to approach 1/2 in 1235. Maximum Profit in Job Scheduling.
        '''
        events = sorted((e, s, v) for s, e, v in events)
        n = len(events)
        f = [[0] * (k + 1) for _ in range(n + 1)]

        def prev(x):
            start = events[x][1]
            return bisect_right(events, (start - 1, inf)) - 1

        for i in range(n):
            p = prev(i) + 1
            for j in range(k + 1):
                f[i + 1][j] = f[i][j] # skip event i
                if j - 1 >= 0: # join event i
                    f[i + 1][j] = max(f[i + 1][j], f[p][j-1] + events[i][2])
        return max(f[-1])
        '''
        DP with optimized space.
        Above transition: f[i+1][j] = max(f[i][j], f[p][j-1] + events[i][2])

        The latest f[i+1][j] depends on f[i][j] and f[p][j-1], there's no way
        to reduce one dimension of space. But if we can swap the two
        dimensions, so that f[j][i+1] = max(f[j][i], f[j-1][p] + events[i][2]),
        we make f[i+1] depends on f[i] and f'[p] where f' is the previous f.

        Now we can use 2 rolling arrays to record f[i] and f'.

        Below is the swapped version without rolling arrays. Rolling array is
        trivial based on this.

        Time: O(n log(n) + kn)
        Space: O(n)
        '''
        events = sorted((e, s, v) for s, e, v in events)
        n = len(events)
        f = [[0] * (n + 1) for _ in range(k + 1)]

        @cache
        def prev(x):
            start = events[x][1]
            return bisect_right(events, (start - 1, inf)) - 1

        ans = 0
        for j in range(k+1):
            for i in range(n):
                p = prev(i) + 1
                f[j][i + 1] = f[j][i] # skip event i
                if j - 1 >= 0: # join event i
                    f[j][i + 1] = max(f[j][i + 1], f[j-1][p] + events[i][2])
                ans = max(ans, f[j][i + 1])

        return ans
        '''
        Another implementation style similar to the second DP style in 1235.
        Theoretical time complexity is slightly higher, but runs faster.

        Time: O(kn log(n))
        Space: O(n)
        '''
        events = sorted((e, s, v) for s, e, v in events)
        f = [[0, 0]]
        for _ in range(k):
            f2 = [[0, 0]]
            for e, s, v in events:
                i = bisect_right(f, [s, -inf]) - 1
                if f[i][1] + v > f2[-1][1]:
                    f2.append([e, f[i][1] + v])
            f = f2
        return f[-1][-1]