# 1585. Check If String Is Transformable With Substring Sort Operations
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        '''
        Bubble sort.
        Sorting a subarray is the same as sorting multiple pairs.
        Transforming s into t is to make sure every digit in s that makes
        the digit in t can move left in s, without breaking bubble rule.
        For a given digit d at pos p, if there's a char d0 in s such that
        d0 < d and its pos p0 < p, we can't transform because d cannot bypass
        d0. On the other hand, if there's no such d0, then we can sort the
        interval in s[p1: p+1] where p1 is the position in t. And we don't
        really need to sort.

        Time: O(n) where n is len(s), the inner loop can only run 9 times in
              each round.
        Space: O(n)
        '''
        s_pos = defaultdict(deque)
        s = [int(c) for c in s]
        t = [int(c) for c in t]
        for i, c in enumerate(s):
            s_pos[c].append(i)
        for c in t:
            if not s_pos[c]:
                return False
            pos = s_pos[c].popleft()
            if any(s_pos[x] and s_pos[x][0] < pos for x in range(c)):
                return False
        return True