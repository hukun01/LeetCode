# 1782. Count Pairs Of Nodes
class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        '''
        Sort.
        The key in this solution is to do below logic faster:
        Counting the number of `count[a] + count[b] - count[(a, b)] > x`.
        
        Notice that the number of queries is small, so we focus on answering
        one query. Count the number of edges for each node, and the count of
        shared edges for each node pair (at most have E pairs where E is the
        number of edges).

        Now we need to leverage this two data to quickly find out the above
        count under conditions. A naive way is to go through a double for-loop
        to try all possible (a, b) and count, but that takes O(n^2) time and
        is too slow. A better way is to break down the equation into two parts.
        1. count[a] + count[b]
        2. count[(a, b)]
        We calculate #1 and #2 separately, and combine them.
        To calculate #1 efficiently, we sort the count into sorted_count, and
        accumulate the number of edges [left, right], 
        whose `sorted_count[left] + sorted_count[right] > q`.
        Then we go through all existing edges (instead of all possible node
        pairs), and minus one if `q < count[a] + count[b] <= q + shared_count`.

        Time: O(q * (n+E))
        Space: O(n + E)
        '''
        count = [0] * (n + 1)
        shared = Counter()
        for a, b in edges:
            count[a] += 1
            count[b] += 1
            shared[tuple(sorted([a, b]))] += 1

        sorted_count = sorted(count)
        ans = [0] * len(queries)
        for i, q in enumerate(queries):
            left, right = 1, n
            while left < right:
                if sorted_count[left] + sorted_count[right] > q:
                    ans[i] += right - left
                    right -= 1
                else:
                    left += 1

            for (a, b), shared_count in shared.items():
                if q < count[a] + count[b] <= q + shared_count:
                    ans[i] -= 1

        return ans