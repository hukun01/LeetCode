# 1284. Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        '''
        BFS.
        The key observation is that R and C are very small.
        Similar to 773. Sliding Puzzle.
        '''
        R, C = len(mat), len(mat[0])
        target = '0' * (R * C)
        def to_state(arr1d):
            return ''.join(str(c) for c in arr1d)

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def flip(r, c,state):
            ans = [int(c) for c in state]
            ans[r * C + c] ^= 1
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if not 0 <= nr < R or not 0 <= nc < C:
                    continue
                ans[nr * C + nc] ^= 1
            return to_state(ans)

        visited = set()
        start = to_state([cell for cell in itertools.chain(*mat)])
        queue = deque([start])
        steps = 0
        while queue:
            for _ in range(len(queue)):
                state = queue.popleft()
                if state == target:
                    return steps
                if state in visited:
                    continue
                visited.add(state)
                for r in range(R):
                    for c in range(C):
                        queue.append(flip(r,c,state))
            steps += 1
        return -1