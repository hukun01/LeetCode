# 514. Freedom Trail
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        '''
        1/2 DFS with memoization.
        Kinda of brute force DFS.
        '''
        n = len(ring)
        @functools.lru_cache(None)
        def dfs(ringIdx, keyIdx):
            if keyIdx == len(key):
                return 0
            if ringIdx < 0:
                ringIdx += n
            leftIdx = rightIdx = ringIdx
            leftSteps = rightSteps = 0
            while ring[leftIdx] != key[keyIdx]:
                leftIdx -= 1
                leftSteps += 1
            while ring[rightIdx] != key[keyIdx]:
                rightIdx = (rightIdx + 1) % n
                rightSteps += 1
            left = leftSteps + 1 + dfs(leftIdx, keyIdx + 1)
            right = rightSteps + 1 + dfs(rightIdx, keyIdx + 1)
            return min(left, right)
        return dfs(0, 0)
        '''
        2/2 DP.
        '''
        # the distance between two points (i, j) on the ring
        def dist(i, j):
            return min(abs(i - j), len(ring) - abs(i - j))
        # build the position list for each character in ring
        pos = collections.defaultdict(list)
        for i, c in enumerate(ring):
            pos[c].append(i)
        # the current possible state: {position of the ring: the cost}
        state = {0: 0}
        for c in key:
            next_state = {}
            for j in pos[c]:  # every possible target position
                next_state[j] = float('inf')
                for i in state:  # every possible start position
                    next_state[j] = min(next_state[j], dist(i, j) + state[i])
            state = next_state
        return min(state.values()) + len(key)