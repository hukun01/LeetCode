# 1654. Minimum Jumps to Reach Home
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        '''
        BFS.
        There 2 keys here:
        1. Need to keep track of (cur, back) in visited, instead of just 'cur'.
        2. Need to define an upper bound for the 'cur', otherwise we can keep
        going forward indefinitely. This upper bound should be
        (max(forbidden + [x]) + a + b), as we may need to go beyond 'x' by
        less than 'a + b', this can only happen when a < b. For example, at
        (x-1), we already backed once, so now we can only go right by 'a',
        since a < b, we can't go left now as we would just lost progress,
        we will keep going right for k times until ka >= b, this is equivalent
        to 'a + b' when working as upper bound.
        Also, when we come back, we can't land at any position in forbidden,
        so the upper bound needs to be greater than max(forbidden) + a + b.
        Alternatively, we can use 6001 as the upper bound based on data range.

        Time: O(E + V) where E is the number of edges in the search graph,
        V is the number of verticies in the graph. E is (x/a * x/b), V is
        approximate to E as each node has no more than 2 outdegrees.
        Space: O(V)
        '''
        f = set(forbidden)
        q = deque([(0, 0)]) # (cur, back)
        steps = 0
        visited = set()
        upper = max(f | {x}) + a + b
        while q:
            for _ in range(len(q)):
                cur, back = q.popleft()
                if cur in f or cur < 0 or (cur, back) in visited:
                    continue
                if cur > upper:
                    continue
                if cur == x:
                    return steps
                visited.add((cur, back))
                q.append((cur + a, 0))
                if back == 0:
                    q.append((cur - b, 1))
            steps += 1
        return -1