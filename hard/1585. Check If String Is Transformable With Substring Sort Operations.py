# 1585. Check If String Is Transformable With Substring Sort Operations
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        '''
        Bubble sort.
        Sorting a subarray is the same as sorting multiple pairs.
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
            for x in range(c):
                if s_pos[x] and s_pos[x][0] < pos:
                    return False
        return True